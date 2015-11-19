path = "/opt/flexget/config.yml"
default = dict(
    tasks = dict(
	rss = dict(
	    template = "tv",
	    rss = "URL"
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
            )
        )
    )
)
default['templates']['tv']['configure_series']['from'] = dict(
                        trakt_list = dict(
                            username = "trakt_user",
                            list = "flexget",
                            type = "shows"
                        )
                    )