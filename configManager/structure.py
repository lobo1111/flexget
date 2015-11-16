path = "/opt/flexget/config.yml"
default = dict(
    tasks = dict(),
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