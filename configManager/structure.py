path = "/opt/flexget/config.yml"
default = dict(
    tasks = dict(
	ezrs = dict(
	    template = "tv",
	    rss = "https://eztv.ag/ezrss.xml"
	)
    ),
    templates = dict(
        tv = dict(
            download = "/opt/torrents",
            configure_series = dict(
                settings = dict(
                    identified_by = "ep",
                    quality = "720p",
                    timeframe = "1 hours"
                ),
                from = dict(
		    trakt_list = dict(
		        username = "lobo1111",
			list = "flexget",
			type = "shows"
		    )
		) 
            )
        )
    )
)
