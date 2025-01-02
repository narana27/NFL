import scrapy
import math

class DropdownSpider(scrapy.Spider):
    name = "SeasonStatsSpider"
    allowed_domains = ["footballguys.com"]
    start_urls = ["https://www.footballguys.com/stats/season/teams?team=ARI&year=2023"]

    def parse(self, response):
        player_names = response.css("div#stats_season_data tbody td.name-col a::text").getall()
        #player_team= response.css("")
        player_pos = ["QB","RB","WR","TE", "DT", "DE", "LB", 'CB', "S", "K" ]
        #dictionary containing "QB:2,RB:3,etc
        team_pos = {
            position:[len(response.css(f"div#stats_season_data div.table-responsive:nth-of-type({index+1}) tbody td.name-col a::text").getall()), response.css(f"div#stats_season_data div.table-responsive:nth-of-type({index+1}) tbody td.data-col::text").getall()]
            for index, position in enumerate(player_pos, start=0)
        }
        #leads to Stats_labels to hold the values of each stat
        pos_stat_label = {
            position: response.css(
                           f"div#stats_season_data div.table-responsive:nth-of-type({index + 1}) thead th.data-header::text").getall()
            for index, position in enumerate(player_pos, start=0)
        }
        yield pos_stat_label

        #max len is known for all values
        max_len_stat = 12
        for position, list in team_pos.items():
            stat_list = list[1]
            len_stat = int(len(stat_list)/list[0])
            diff = max_len_stat-len_stat
            if len_stat< max_len_stat:
                place = len_stat
                for i in range((diff)*list[0]):
                    team_pos[position][1].insert(place, 'NA')
                    if ((i+1)%diff==0 and i!=0) or (i==0 and diff ==1):
                        place+= (len_stat)
                    place+=1

        #yield team_pos

        i =1
        final_dict = {}
        for name in player_names:
            cum_count = 0
            for position, count in team_pos.items():
                cum_count+=count[0]
                if i <= cum_count:
                    name = name.strip()
                    final_dict["Names"] = name
                    final_dict["Pos"] = position
                    for index, label in enumerate(count[1]):
                        y= 12
                        x= (i-cum_count+count[0]-1)*y
                        if index >=x and index <x+y:
                            label =label.strip()
                            final_dict[index-x]= label
                    yield final_dict
                    break
            i+=1

#stats = response.css("div#stats_season_data tbody td.data-col::text").getall()
    #cleaned_stats = stats.strip(



'''

        
        for value, name in zip(team_values, team_names):
            team_url = f"https://www.footballguys.com/stats/season/teams?team={value}&year=2023"
            yield scrapy.Request(url=team_url, callback=self.parse_team)

    'def parse_team(self, response):
        headers = response.css(
            "div.table-responsive table.table.sortable-table thead tr th::text"
        ).getall()
        rows = response.css("div.table-responsive table.table.sortable-table tbody tr")

        for row in rows:
            cells = row.css("td::text").getall()
            if len(cells) == len(headers):
                player_data = {headers[i]: cells[i] for i in range(len(headers))}
                yield player_data
                '''

class testSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        authors= response.css("small.author::text").getall()
        yield {"list Autors": authors}