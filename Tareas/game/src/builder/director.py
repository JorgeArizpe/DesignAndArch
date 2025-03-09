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