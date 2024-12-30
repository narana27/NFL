import scrapy

class DropdownSpider(scrapy.Spider):
    name = "SeasonStatsSpider"
    allowed_domains = ["footballguys.com"]
    start_urls = ["https://www.footballguys.com/stats/season/teams?team=ARI&year=2023"]

    def parse(self, response):
        player_names = response.css("div#stats_season_data tbody td.name-col a::text").getall()
        qb_num = len(response.css("div#stats_season_data div.table-responsive:nth-of-type(1) tbody td.name-col a::text").getall())
        rb_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(2) tbody td.name-col a::text").getall())
        wr_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(3) tbody td.name-col a::text").getall())
        te_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(4) tbody td.name-col a::text").getall())
        dt_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(5) tbody td.name-col a::text").getall())
        de_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(6) tbody td.name-col a::text").getall())
        lb_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(7) tbody td.name-col a::text").getall())
        s_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(8) tbody td.name-col a::text").getall())
        k_num= len(response.css("div#stats_season_data div.table-responsive:nth-of-type(9) tbody td.name-col a::text").getall())
        stats = response.css("div#stats_season_data tbody td.data-col::text").getall()
        #cleaned_stats = stats.strip()

        i=1
        pos = ""
        for name in player_names:
            if i<=qb_num:
                pos = "QB"
            elif i <= qb_num+rb_num:
                pos = "RB"
            elif i<= qb_num+rb_num+wr_num:
                pos = "WR"
            elif i <= qb_num + rb_num + wr_num + te_num:
                pos = "TE"
            i +=1
            yield {"Name":name, "Pos":pos}

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