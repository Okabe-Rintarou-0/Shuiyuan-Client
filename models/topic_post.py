from typing import Optional
from models.common import *
from dataclasses import dataclass


@dataclass
class ActionsSummary:
    id: int
    can_act: bool
    count: int

    @staticmethod
    def from_dict(obj: Any) -> 'ActionsSummary':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        can_act = from_bool(obj.get("can_act"))
        count = from_int(obj.get("count"))
        return ActionsSummary(id, can_act, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["can_act"] = from_bool(self.can_act)
        result["count"] = from_int(self.count)
        return result


@dataclass
class LinkCount:
    url: str
    internal: bool
    reflection: bool
    title: str
    clicks: int

    @staticmethod
    def from_dict(obj: Any) -> 'LinkCount':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        internal = from_bool(obj.get("internal"))
        reflection = from_bool(obj.get("reflection"))
        title = from_str(obj.get("title"))
        clicks = from_int(obj.get("clicks"))
        return LinkCount(url, internal, reflection, title, clicks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["internal"] = from_bool(self.internal)
        result["reflection"] = from_bool(self.reflection)
        result["title"] = from_str(self.title)
        result["clicks"] = from_int(self.clicks)
        return result


@dataclass
class Option:
    id: str
    html: str
    votes: int

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        html = from_str(obj.get("html"))
        votes = from_int(obj.get("votes"))
        return Option(id, html, votes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["html"] = from_str(self.html)
        result["votes"] = from_int(self.votes)
        return result


@dataclass
class Poll:
    name: str
    type: str
    status: str
    results: str
    options: List[Option]
    voters: int
    chart_type: str
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'Poll':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        type = from_str(obj.get("type"))
        status = from_str(obj.get("status"))
        results = from_str(obj.get("results"))
        options = from_list(Option.from_dict, obj.get("options"))
        voters = from_int(obj.get("voters"))
        chart_type = from_str(obj.get("chart_type"))
        title = from_str(obj.get("title"))
        return Poll(name, type, status, results, options, voters, chart_type, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["type"] = from_str(self.type)
        result["status"] = from_str(self.status)
        result["results"] = from_str(self.results)
        result["options"] = from_list(
            lambda x: to_class(Option, x), self.options)
        result["voters"] = from_int(self.voters)
        result["chart_type"] = from_str(self.chart_type)
        result["title"] = from_str(self.title)
        return result


@dataclass
class PollsVotes:
    poll: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'PollsVotes':
        assert isinstance(obj, dict)
        poll = from_list(from_str, obj.get("poll"))
        return PollsVotes(poll)

    def to_dict(self) -> dict:
        result: dict = {}
        result["poll"] = from_list(from_str, self.poll)
        return result


@dataclass
class ReplyToUser:
    username: str
    name: str
    avatar_template: str

    @staticmethod
    def from_dict(obj: Any) -> 'ReplyToUser':
        assert isinstance(obj, dict)
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        return ReplyToUser(username, name, avatar_template)

    def to_dict(self) -> dict:
        result: dict = {}
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        return result


@dataclass
class Retort:
    post_id: int
    usernames: List[str]
    emoji: str

    @staticmethod
    def from_dict(obj: Any) -> 'Retort':
        assert isinstance(obj, dict)
        post_id = from_int(obj.get("post_id"))
        usernames = from_list(from_str, obj.get("usernames"))
        emoji = from_str(obj.get("emoji"))
        return Retort(post_id, usernames, emoji)

    def to_dict(self) -> dict:
        result: dict = {}
        result["post_id"] = from_int(self.post_id)
        result["usernames"] = from_list(from_str, self.usernames)
        result["emoji"] = from_str(self.emoji)
        return result


@dataclass
class Post:
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: datetime
    cooked: str
    post_number: int
    post_type: int
    updated_at: datetime
    reply_count: int
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: float
    yours: bool
    topic_id: int
    topic_slug: str
    display_username: str
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    read: bool
    bookmarked: bool
    actions_summary: List[ActionsSummary]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    hidden: bool
    trust_level: int
    deleted_at: str
    user_deleted: bool
    edit_reason: str
    can_view_edit_history: bool
    wiki: bool
    user_cakedate: datetime
    can_accept_answer: bool
    can_unaccept_answer: bool
    accepted_answer: bool
    topic_accepted_answer: bool
    retorts: List[Retort]
    reply_to_post_number: int
    primary_group_name: str
    flair_name: str
    flair_url: str
    flair_bg_color: str
    flair_color: str
    flair_group_id: int
    link_counts: List[LinkCount]
    user_title: str
    title_is_group: bool
    polls: List[Poll]
    polls_votes: Optional[PollsVotes] = None
    reply_to_user: Optional[ReplyToUser] = None
    user_birthdate: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        username = from_str(obj.get("username"))
        avatar_template = from_str(obj.get("avatar_template"))
        created_at = from_datetime(obj.get("created_at"))
        cooked = from_str(obj.get("cooked"))
        post_number = from_int(obj.get("post_number"))
        post_type = from_int(obj.get("post_type"))
        updated_at = from_datetime(obj.get("updated_at"))
        reply_count = from_int(obj.get("reply_count"))
        quote_count = from_int(obj.get("quote_count"))
        incoming_link_count = from_int(obj.get("incoming_link_count"))
        reads = from_int(obj.get("reads"))
        readers_count = from_int(obj.get("readers_count"))
        score = from_float(obj.get("score"))
        yours = from_bool(obj.get("yours"))
        topic_id = from_int(obj.get("topic_id"))
        topic_slug = from_str(obj.get("topic_slug"))
        display_username = from_str(obj.get("display_username"))
        version = from_int(obj.get("version"))
        can_edit = from_bool(obj.get("can_edit"))
        can_delete = from_bool(obj.get("can_delete"))
        can_recover = from_bool(obj.get("can_recover"))
        can_see_hidden_post = from_bool(obj.get("can_see_hidden_post"))
        can_wiki = from_bool(obj.get("can_wiki"))
        read = from_bool(obj.get("read"))
        bookmarked = from_bool(obj.get("bookmarked"))
        actions_summary = from_list(
            ActionsSummary.from_dict, obj.get("actions_summary"))
        moderator = from_bool(obj.get("moderator"))
        admin = from_bool(obj.get("admin"))
        staff = from_bool(obj.get("staff"))
        user_id = from_int(obj.get("user_id"))
        hidden = from_bool(obj.get("hidden"))
        trust_level = from_int(obj.get("trust_level"))
        deleted_at = from_str(obj.get("deleted_at"))
        user_deleted = from_bool(obj.get("user_deleted"))
        edit_reason = from_str(obj.get("edit_reason"))
        can_view_edit_history = from_bool(obj.get("can_view_edit_history"))
        wiki = from_bool(obj.get("wiki"))
        user_cakedate = from_datetime(obj.get("user_cakedate"))
        can_accept_answer = from_bool(obj.get("can_accept_answer"))
        can_unaccept_answer = from_bool(obj.get("can_unaccept_answer"))
        accepted_answer = from_bool(obj.get("accepted_answer"))
        topic_accepted_answer = from_bool(obj.get("topic_accepted_answer"))
        retorts = from_list(Retort.from_dict, obj.get("retorts"))
        reply_to_post_number = from_int(obj.get("reply_to_post_number"))
        primary_group_name = from_str(obj.get("primary_group_name"))
        flair_name = from_str(obj.get("flair_name"))
        flair_url = from_str(obj.get("flair_url"))
        flair_bg_color = from_str(obj.get("flair_bg_color"))
        flair_color = from_str(obj.get("flair_color"))
        flair_group_id = from_int(obj.get("flair_group_id"))
        link_counts = from_list(LinkCount.from_dict, obj.get("link_counts"))
        user_title = from_str(obj.get("user_title"))
        title_is_group = from_bool(obj.get("title_is_group"))
        polls = from_list(Poll.from_dict, obj.get("polls"))
        polls_votes = from_union(
            [PollsVotes.from_dict, from_none], obj.get("polls_votes"))
        reply_to_user = from_union(
            [ReplyToUser.from_dict, from_none], obj.get("reply_to_user"))
        user_birthdate = from_union(
            [from_datetime, from_none], obj.get("user_birthdate"))
        return Post(id, name, username, avatar_template, created_at, cooked, post_number, post_type, updated_at, reply_count, quote_count, incoming_link_count, reads, readers_count, score, yours, topic_id, topic_slug, display_username, version, can_edit, can_delete, can_recover, can_see_hidden_post, can_wiki, read, bookmarked, actions_summary, moderator, admin, staff, user_id, hidden, trust_level, deleted_at, user_deleted, edit_reason, can_view_edit_history, wiki, user_cakedate, can_accept_answer, can_unaccept_answer, accepted_answer, topic_accepted_answer, retorts, reply_to_post_number, primary_group_name, flair_name, flair_url, flair_bg_color, flair_color, flair_group_id, link_counts, user_title, title_is_group, polls, polls_votes, reply_to_user, user_birthdate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["username"] = from_str(self.username)
        result["avatar_template"] = from_str(self.avatar_template)
        result["created_at"] = self.created_at.isoformat()
        result["cooked"] = from_str(self.cooked)
        result["post_number"] = from_int(self.post_number)
        result["post_type"] = from_int(self.post_type)
        result["updated_at"] = self.updated_at.isoformat()
        result["reply_count"] = from_int(self.reply_count)
        result["quote_count"] = from_int(self.quote_count)
        result["incoming_link_count"] = from_int(self.incoming_link_count)
        result["reads"] = from_int(self.reads)
        result["readers_count"] = from_int(self.readers_count)
        result["score"] = from_float(self.score)
        result["yours"] = from_bool(self.yours)
        result["topic_id"] = from_int(self.topic_id)
        result["topic_slug"] = from_str(self.topic_slug)
        result["display_username"] = from_str(self.display_username)
        result["version"] = from_int(self.version)
        result["can_edit"] = from_bool(self.can_edit)
        result["can_delete"] = from_bool(self.can_delete)
        result["can_recover"] = from_bool(self.can_recover)
        result["can_see_hidden_post"] = from_bool(self.can_see_hidden_post)
        result["can_wiki"] = from_bool(self.can_wiki)
        result["read"] = from_bool(self.read)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["actions_summary"] = from_list(
            lambda x: to_class(ActionsSummary, x), self.actions_summary)
        result["moderator"] = from_bool(self.moderator)
        result["admin"] = from_bool(self.admin)
        result["staff"] = from_bool(self.staff)
        result["user_id"] = from_int(self.user_id)
        result["hidden"] = from_bool(self.hidden)
        result["trust_level"] = from_int(self.trust_level)
        result["deleted_at"] = from_str(self.deleted_at)
        result["user_deleted"] = from_bool(self.user_deleted)
        result["edit_reason"] = from_str(self.edit_reason)
        result["can_view_edit_history"] = from_bool(self.can_view_edit_history)
        result["wiki"] = from_bool(self.wiki)
        result["user_cakedate"] = self.user_cakedate.isoformat()
        result["can_accept_answer"] = from_bool(self.can_accept_answer)
        result["can_unaccept_answer"] = from_bool(self.can_unaccept_answer)
        result["accepted_answer"] = from_bool(self.accepted_answer)
        result["topic_accepted_answer"] = from_bool(self.topic_accepted_answer)
        result["retorts"] = from_list(
            lambda x: to_class(Retort, x), self.retorts)
        result["reply_to_post_number"] = from_int(self.reply_to_post_number)
        result["primary_group_name"] = from_str(self.primary_group_name)
        result["flair_name"] = from_str(self.flair_name)
        result["flair_url"] = from_str(self.flair_url)
        result["flair_bg_color"] = from_str(self.flair_bg_color)
        result["flair_color"] = from_str(self.flair_color)
        result["flair_group_id"] = from_int(self.flair_group_id)
        result["link_counts"] = from_list(
            lambda x: to_class(LinkCount, x), self.link_counts)
        result["user_title"] = from_str(self.user_title)
        result["title_is_group"] = from_bool(self.title_is_group)
        result["polls"] = from_list(lambda x: to_class(Poll, x), self.polls)
        result["polls_votes"] = from_union(
            [lambda x: to_class(PollsVotes, x), from_none], self.polls_votes)
        result["reply_to_user"] = from_union(
            [lambda x: to_class(ReplyToUser, x), from_none], self.reply_to_user)
        result["user_birthdate"] = from_union(
            [lambda x: x.isoformat(), from_none], self.user_birthdate)
        return result


@dataclass
class PostStream:
    posts: List[Post]

    @staticmethod
    def from_dict(obj: Any) -> 'PostStream':
        assert isinstance(obj, dict)
        posts = from_list(Post.from_dict, obj.get("posts"))
        return PostStream(posts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["posts"] = from_list(lambda x: to_class(Post, x), self.posts)
        return result


@dataclass
class TopicPosts:
    post_stream: PostStream
    id: int

    @staticmethod
    def from_dict(obj: Any) -> 'TopicPosts':
        assert isinstance(obj, dict)
        post_stream = PostStream.from_dict(obj.get("post_stream"))
        id = from_int(obj.get("id"))
        return TopicPosts(post_stream, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["post_stream"] = to_class(PostStream, self.post_stream)
        result["id"] = from_int(self.id)
        return result


def topic_posts_from_dict(s: Any) -> TopicPosts:
    return TopicPosts.from_dict(s)


def topic_posts_to_dict(x: TopicPosts) -> Any:
    return to_class(TopicPosts, x)
