import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function showPetPanel(
    context: vscode.ExtensionContext,
    suggestion: string,
    characterGif: string | any,
) {
    const panel = vscode.window.createWebviewPanel(
        'code analyzer',
        'Code Analyzer',
        vscode.ViewColumn.Two,
        {
            enableScripts: true,
            localResourceRoots: [vscode.Uri.joinPath(context.extensionUri, 'media')],
        }
    );

    const getUri = (fileName: string) => {
        return panel.webview.asWebviewUri(
            vscode.Uri.joinPath(context.extensionUri, 'media', fileName)
        );
    }

    const characterGifUri = getUri(characterGif);

    const htmlPath = path.join(context.extensionPath, 'media', 'panel.html');

    let html = fs.readFileSync(htmlPath, 'utf8');

    html = html.replace("%SUGGESTION%", suggestion).replace("%GIF%", characterGifUri.toString());

    panel.webview.html = html;
}