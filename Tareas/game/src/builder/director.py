class EnemyDirector:
    def construct_enemy(self, builder, enemy_type='normal'):
        builder.reset()
        builder.set_position()
        if enemy_type == 'normal':
            builder.set_sprite('../assets/images/enemy.png')
            builder.set_speed(2)
            builder.set_points(10)
        elif enemy_type == 'fast':
            builder.set_sprite('../assets/images/red.png')
            builder.set_speed(4)
            builder.set_points(20)
        elif enemy_type == 'strong':
            builder.set_sprite('../assets/images/green.png')
            builder.set_speed(3)
            builder.set_points(30)
        return builder.get_enemy()

class PlayerDirector:
    def construct_player(self, builder, tipo = 1, x = 400, y = 500):
        builder.reset()
        builder.set_position(x, y)
        if tipo == 1:
            builder.set_speed(9)
            builder.set_bullet_speed(12)
            builder.set_score_mult(1)
        elif tipo == 2:
            builder.set_speed(7)
            builder.set_bullet_speed(10)
            builder.set_score_mult(1.2)
        elif tipo == 3:
            builder.set_speed(5)
            builder.set_bullet_speed(7)
            builder.set_score_mult(1.5)
        return builder.get_player()