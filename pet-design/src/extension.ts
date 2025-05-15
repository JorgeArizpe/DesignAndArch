// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import axios from 'axios';
import * as vscode from 'vscode';
import { showPetPanel } from './showPetPanel';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

const characters = [
	{
		prompt: "You are the virutal diva Hatsune Miku and you are reviewing code, be mean and criticize everything but push to improve the code, dont provide code just base the feedback on design patterns.",
		gif: "https://tenor.com/hKaWulNc9Ja.gif",
		name: "Hatsune Miku"
	},
	{
		prompt: "You are the virutal diva Kasane Teto and you are reviewing code, be fair and criticize midly but push to improve the code, dont provide code just base the feedback on design patterns.",
		gif: "https://tenor.com/osGLinbfRMo.gif",
		name: "Kasane Teto"
	},
	{
		prompt: "You are the Kazuma kiryu and you are reviewing code, be kind and encouraging push to improve the code, dont provide code just base the feedback on design patterns.",
		gif: "https://tenor.com/8fWLk2KXX6.gif",
		name: "Kazuma Kiryu"
	}
];

export const analyzeCodeWithGemini = async (code: string, characters: { prompt: string; gif: string; name: string }) => {
	const apiKey = process.env.GEMINI_API_KEY; 
	if (!apiKey) {
		vscode.window.showErrorMessage('GEMINI_API_KEY is not set. Please set it in your environment variables.');
		return;
	}
	try {
		const response = await axios.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key='
			+ apiKey,
			{
				contents: [
					{
						parts: [{ text: `${characters?.prompt} ${code}` }],
					}
				]
			},
			{ headers: { 'Content-Type': 'application/json' } }
		);
		return response.data.candidates[0].parts?.[0].text;
	} catch (error) {
		console.error('Error analyzing code with Gemini:', error);
		vscode.window.showErrorMessage('Error analyzing code with Gemini. Please check the console for more details.');
		return "Error analyzing code with Gemini.";
	}
}

export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "pet-design" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = vscode.commands.registerCommand('pet-design.helloWorld', async () => {
        vscode.window.showInformationMessage('Hello World from pet-design!');

        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage('No active window.');
            return;
        }

        const selectedCharacter = await vscode.window.showQuickPick(
            characters.map((character) => character.name),
            { placeHolder: 'Select a character' }
        );

        if (!selectedCharacter) {
            vscode.window.showErrorMessage('No character selected.');
            return;
        }

        const character = characters.find((character) => character.name === selectedCharacter);

        if (!character) {
            vscode.window.showErrorMessage('Character not found.');
            return;
        }

        const code = editor.document.getText();
        vscode.window.showInformationMessage(`Analyzing code...`);

        const analysis = await analyzeCodeWithGemini(code, character);
        showPetPanel(context, analysis, character.gif);
    });
	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() { }
