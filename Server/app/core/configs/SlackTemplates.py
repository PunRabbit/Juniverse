from dataclasses import dataclass, field


@dataclass(frozen=False)
class SlackTemplates:
    TEST_TEMPLATES: dict = field(default_factory=lambda: dict(
        test_template=[
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🧪 Test Run with Server Test Code",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ""
                }
            },
            {
                "type": "divider"
            }
        ]

    )
                                 )
