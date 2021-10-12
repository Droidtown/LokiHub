class DataPuller():
    def get_player_single_game_stats(stat, player_name, season):
        query = f"""
            select 
            team, 
            player_name, 
            {stat} as target_stat
            from df 
            where season = {season}
            and player_name = '{player_name}'
            order by {stat} desc
            limit 1
        """
        print(query)
        return query

    def get_player_agg_stats(stat, player_name, season):
        query = f"""
            select 
            team, 
            player_name, 
            sum({stat}) as agg_stats, 
            count(game_id) as total_games,
            sum({stat}) / count(game_id) as target_stat
            from df 
            where season = {season}
            and player_name = '{player_name}'
            group by team, player_name
        """
        print(query)
        return query

    def get_team_best_player_stats(stat, team, season):
        query = f"""
            select 
            player_name, 
            sum({stat}) as agg_stats, 
            count(game_id) as total_games,
            sum({stat}) / count(game_id) as target_stat
            from df 
            where season = {season}
            and team = '{team}'
            group by player_name
            order by agg_stats desc
            limit 1
        """
        print(query)
        return query

    def get_multiple_games_stats(num_games, stat, value, team, year):
        query = f"""
            select 
            player_name, 
            count(distinct game_id) as total_games
            from df 
            where {stat} > {value}
            and season = {year}
            and team = '{team}'
            group by player_name
            order by total_games desc
        """
        return query
