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
            series = dict(
                settings = dict(
                    default = dict(
                        identified_by = "ep",
                        quality = "720p",
                        timeframe = "1 hours"
                    )
                ),
                default = []
            )
        )
    )
)
