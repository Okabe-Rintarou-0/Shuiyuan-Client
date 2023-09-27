from typing import Optional
from models.common import *
from dataclasses import dataclass


@dataclass
class ActionsSummary:
    id: int
    can_act: Optional[bool]
    count: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> 'ActionsSummary':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        can_act = from_union([from_bool, from_none], obj.get("can_act"))
        count = from_union([from_int, from_none], obj.get("count"))
        return ActionsSummary(id, can_act, count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["can_act"] = from_union([from_bool, from_none], self.can_act)
        result["count"] = from_union([from_int, from_none], self.count)
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
    reply_to_post_number: Optional[int]
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: int
    yours: bool
    topic_id: int
    topic_slug: str
    display_username: str
    primary_group_name: None
    flair_name: None
    flair_url: None
    flair_bg_color: None
    flair_color: None
    flair_group_id: None
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    user_title: str
    reply_to_user: Optional[ReplyToUser]
    bookmarked: bool
    raw: str
    actions_summary: List[ActionsSummary]
    moderator: bool
    admin: bool
    staff: bool
    user_id: int
    hidden: bool
    trust_level: int
    deleted_at: None
    user_deleted: bool
    edit_reason: None
    can_view_edit_history: bool
    wiki: bool
    user_cakedate: datetime
    can_accept_answer: bool
    can_unaccept_answer: bool
    accepted_answer: bool
    topic_accepted_answer: bool
    retorts: List[Any]

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
        reply_to_post_number = from_union(
            [from_int, from_none], obj.get("reply_to_post_number"))
        quote_count = from_int(obj.get("quote_count"))
        incoming_link_count = from_int(obj.get("incoming_link_count"))
        reads = from_int(obj.get("reads"))
        readers_count = from_int(obj.get("readers_count"))
        score = from_float(obj.get("score"))
        yours = from_bool(obj.get("yours"))
        topic_id = from_int(obj.get("topic_id"))
        topic_slug = from_str(obj.get("topic_slug"))
        display_username = from_str(obj.get("display_username"))
        primary_group_name = from_none(obj.get("primary_group_name"))
        flair_name = from_none(obj.get("flair_name"))
        flair_url = from_none(obj.get("flair_url"))
        flair_bg_color = from_none(obj.get("flair_bg_color"))
        flair_color = from_none(obj.get("flair_color"))
        flair_group_id = from_none(obj.get("flair_group_id"))
        version = from_int(obj.get("version"))
        can_edit = from_bool(obj.get("can_edit"))
        can_delete = from_bool(obj.get("can_delete"))
        can_recover = from_bool(obj.get("can_recover"))
        can_see_hidden_post = from_bool(obj.get("can_see_hidden_post"))
        can_wiki = from_bool(obj.get("can_wiki"))
        user_title = from_str(obj.get("user_title"))
        reply_to_user = from_union(
            [ReplyToUser.from_dict, from_none], obj.get("reply_to_user"))
        bookmarked = from_bool(obj.get("bookmarked"))
        raw = from_str(obj.get("raw"))
        actions_summary = from_list(
            ActionsSummary.from_dict, obj.get("actions_summary"))
        moderator = from_bool(obj.get("moderator"))
        admin = from_bool(obj.get("admin"))
        staff = from_bool(obj.get("staff"))
        user_id = from_int(obj.get("user_id"))
        hidden = from_bool(obj.get("hidden"))
        trust_level = from_int(obj.get("trust_level"))
        deleted_at = from_none(obj.get("deleted_at"))
        user_deleted = from_bool(obj.get("user_deleted"))
        edit_reason = from_none(obj.get("edit_reason"))
        can_view_edit_history = from_bool(obj.get("can_view_edit_history"))
        wiki = from_bool(obj.get("wiki"))
        user_cakedate = from_datetime(obj.get("user_cakedate"))
        can_accept_answer = from_bool(obj.get("can_accept_answer"))
        can_unaccept_answer = from_bool(obj.get("can_unaccept_answer"))
        accepted_answer = from_bool(obj.get("accepted_answer"))
        topic_accepted_answer = from_bool(obj.get("topic_accepted_answer"))
        retorts = from_list(lambda x: x, obj.get("retorts"))
        return Post(id, name, username, avatar_template, created_at, cooked, post_number, post_type, updated_at, reply_count, reply_to_post_number, quote_count, incoming_link_count, reads, readers_count, score, yours, topic_id, topic_slug, display_username, primary_group_name, flair_name, flair_url, flair_bg_color, flair_color, flair_group_id, version, can_edit, can_delete, can_recover, can_see_hidden_post, can_wiki, user_title, reply_to_user, bookmarked, raw, actions_summary, moderator, admin, staff, user_id, hidden, trust_level, deleted_at, user_deleted, edit_reason, can_view_edit_history, wiki, user_cakedate, can_accept_answer, can_unaccept_answer, accepted_answer, topic_accepted_answer, retorts)

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
        result["reply_to_post_number"] = from_union(
            [from_none, from_int], self.reply_to_post_number)
        result["quote_count"] = from_int(self.quote_count)
        result["incoming_link_count"] = from_int(self.incoming_link_count)
        result["reads"] = from_int(self.reads)
        result["readers_count"] = from_int(self.readers_count)
        result["score"] = from_float(self.score)
        result["yours"] = from_bool(self.yours)
        result["topic_id"] = from_int(self.topic_id)
        result["topic_slug"] = from_str(self.topic_slug)
        result["display_username"] = from_str(self.display_username)
        result["primary_group_name"] = from_none(self.primary_group_name)
        result["flair_name"] = from_none(self.flair_name)
        result["flair_url"] = from_none(self.flair_url)
        result["flair_bg_color"] = from_none(self.flair_bg_color)
        result["flair_color"] = from_none(self.flair_color)
        result["flair_group_id"] = from_none(self.flair_group_id)
        result["version"] = from_int(self.version)
        result["can_edit"] = from_bool(self.can_edit)
        result["can_delete"] = from_bool(self.can_delete)
        result["can_recover"] = from_bool(self.can_recover)
        result["can_see_hidden_post"] = from_bool(self.can_see_hidden_post)
        result["can_wiki"] = from_bool(self.can_wiki)
        result["user_title"] = from_str(self.user_title)
        result["reply_to_user"] = to_class(ReplyToUser, self.reply_to_user)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["raw"] = from_str(self.raw)
        result["actions_summary"] = from_list(
            lambda x: to_class(ActionsSummary, x), self.actions_summary)
        result["moderator"] = from_bool(self.moderator)
        result["admin"] = from_bool(self.admin)
        result["staff"] = from_bool(self.staff)
        result["user_id"] = from_int(self.user_id)
        result["hidden"] = from_bool(self.hidden)
        result["trust_level"] = from_int(self.trust_level)
        result["deleted_at"] = from_none(self.deleted_at)
        result["user_deleted"] = from_bool(self.user_deleted)
        result["edit_reason"] = from_none(self.edit_reason)
        result["can_view_edit_history"] = from_bool(self.can_view_edit_history)
        result["wiki"] = from_bool(self.wiki)
        result["user_cakedate"] = self.user_cakedate.isoformat()
        result["can_accept_answer"] = from_bool(self.can_accept_answer)
        result["can_unaccept_answer"] = from_bool(self.can_unaccept_answer)
        result["accepted_answer"] = from_bool(self.accepted_answer)
        result["topic_accepted_answer"] = from_bool(self.topic_accepted_answer)
        result["retorts"] = from_list(lambda x: x, self.retorts)
        return result


def post_from_dict(s: Any) -> Post:
    return Post.from_dict(s)


def post_to_dict(x: Post) -> Any:
    return to_class(Post, x)
