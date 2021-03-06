from app.common.command import Command
from dataclasses import dataclass
from uuid import UUID


@dataclass
class LikeTweet(Command):
    tweet_id: UUID
    liked_user_id: UUID
