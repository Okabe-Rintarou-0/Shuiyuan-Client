from typing import Optional
from models.common import *
from dataclasses import dataclass


@dataclass
class TopicActionsSummary:
    id: int
    count: int
    hidden: bool
    can_act: bool

    @staticmethod
    def from_dict(obj: Any) -> 'TopicActionsSummary':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        count = from_int(obj.get("count"))
        hidden = from_bool(obj.get("hidden"))
        can_act = from_bool(obj.get("can_act"))
        return TopicActionsSummary(id, count, hidden, can_act)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["count"] = from_int(self.count)
        result["hidden"] = from_bool(self.hidden)
        result["can_act"] = from_bool(self.can_act)
        return result


@dataclass
class CreatedBy:
    id: int
    username: str
    name: str
    avatar_template: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreatedBy':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        return CreatedBy(id, username, name, avatar_template)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        return result


@dataclass
class Participant:
    id: int
    username: str
    name: str
    avatar_template: str
    post_count: int
    primary_group_name: str
    flair_name: str
    flair_url: str
    flair_color: str
    flair_bg_color: str
    flair_group_id: int
    admin: bool
    moderator: bool
    trust_level: int

    @staticmethod
    def from_dict(obj: Any) -> 'Participant':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        post_count = from_int(obj.get("post_count"))
        primary_group_name = from_str(obj.get("primary_group_name"))
        flair_name = from_str(obj.get("flair_name"))
        flair_url = from_str(obj.get("flair_url"))
        flair_color = from_str(obj.get("flair_color"))
        flair_bg_color = from_str(obj.get("flair_bg_color"))
        flair_group_id = from_int(obj.get("flair_group_id"))
        admin = from_bool(obj.get("admin"))
        moderator = from_bool(obj.get("moderator"))
        trust_level = from_int(obj.get("trust_level"))
        return Participant(id, username, name, avatar_template, post_count, primary_group_name, flair_name, flair_url, flair_color, flair_bg_color, flair_group_id, admin, moderator, trust_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        result["post_count"] = from_int(self.post_count)
        result["primary_group_name"] = from_str(self.primary_group_name)
        result["flair_name"] = from_str(self.flair_name)
        result["flair_url"] = from_str(self.flair_url)
        result["flair_color"] = from_str(self.flair_color)
        result["flair_bg_color"] = from_str(self.flair_bg_color)
        result["flair_group_id"] = from_int(self.flair_group_id)
        result["admin"] = from_bool(self.admin)
        result["moderator"] = from_bool(self.moderator)
        result["trust_level"] = from_int(self.trust_level)
        return result


@dataclass
class Details:
    can_edit: bool
    notification_level: int
    can_move_posts: bool
    can_delete: bool
    can_remove_allowed_users: bool
    can_create_post: bool
    can_reply_as_new_topic: bool
    can_invite_to: bool
    can_invite_via_email: bool
    can_flag_topic: bool
    can_convert_topic: bool
    can_review_topic: bool
    can_close_topic: bool
    can_archive_topic: bool
    can_split_merge_topic: bool
    can_edit_staff_notes: bool
    can_toggle_topic_visibility: bool
    can_pin_unpin_topic: bool
    can_moderate_category: bool
    can_remove_self_id: int
    participants: List[Participant]
    created_by: CreatedBy
    last_poster: CreatedBy

    @staticmethod
    def from_dict(obj: Any) -> 'Details':
        assert isinstance(obj, dict)
        can_edit = from_bool(obj.get("can_edit"))
        notification_level = from_int(obj.get("notification_level"))
        can_move_posts = from_bool(obj.get("can_move_posts"))
        can_delete = from_bool(obj.get("can_delete"))
        can_remove_allowed_users = from_bool(
            obj.get("can_remove_allowed_users"))
        can_create_post = from_bool(obj.get("can_create_post"))
        can_reply_as_new_topic = from_bool(obj.get("can_reply_as_new_topic"))
        can_invite_to = from_bool(obj.get("can_invite_to"))
        can_invite_via_email = from_bool(obj.get("can_invite_via_email"))
        can_flag_topic = from_bool(obj.get("can_flag_topic"))
        can_convert_topic = from_bool(obj.get("can_convert_topic"))
        can_review_topic = from_bool(obj.get("can_review_topic"))
        can_close_topic = from_bool(obj.get("can_close_topic"))
        can_archive_topic = from_bool(obj.get("can_archive_topic"))
        can_split_merge_topic = from_bool(obj.get("can_split_merge_topic"))
        can_edit_staff_notes = from_bool(obj.get("can_edit_staff_notes"))
        can_toggle_topic_visibility = from_bool(
            obj.get("can_toggle_topic_visibility"))
        can_pin_unpin_topic = from_bool(obj.get("can_pin_unpin_topic"))
        can_moderate_category = from_bool(obj.get("can_moderate_category"))
        can_remove_self_id = from_int(obj.get("can_remove_self_id"))
        participants = from_list(
            Participant.from_dict, obj.get("participants"))
        created_by = CreatedBy.from_dict(obj.get("created_by"))
        last_poster = CreatedBy.from_dict(obj.get("last_poster"))
        return Details(can_edit, notification_level, can_move_posts, can_delete, can_remove_allowed_users, can_create_post, can_reply_as_new_topic, can_invite_to, can_invite_via_email, can_flag_topic, can_convert_topic, can_review_topic, can_close_topic, can_archive_topic, can_split_merge_topic, can_edit_staff_notes, can_toggle_topic_visibility, can_pin_unpin_topic, can_moderate_category, can_remove_self_id, participants, created_by, last_poster)

    def to_dict(self) -> dict:
        result: dict = {}
        result["can_edit"] = from_bool(self.can_edit)
        result["notification_level"] = from_int(self.notification_level)
        result["can_move_posts"] = from_bool(self.can_move_posts)
        result["can_delete"] = from_bool(self.can_delete)
        result["can_remove_allowed_users"] = from_bool(
            self.can_remove_allowed_users)
        result["can_create_post"] = from_bool(self.can_create_post)
        result["can_reply_as_new_topic"] = from_bool(
            self.can_reply_as_new_topic)
        result["can_invite_to"] = from_bool(self.can_invite_to)
        result["can_invite_via_email"] = from_bool(self.can_invite_via_email)
        result["can_flag_topic"] = from_bool(self.can_flag_topic)
        result["can_convert_topic"] = from_bool(self.can_convert_topic)
        result["can_review_topic"] = from_bool(self.can_review_topic)
        result["can_close_topic"] = from_bool(self.can_close_topic)
        result["can_archive_topic"] = from_bool(self.can_archive_topic)
        result["can_split_merge_topic"] = from_bool(self.can_split_merge_topic)
        result["can_edit_staff_notes"] = from_bool(self.can_edit_staff_notes)
        result["can_toggle_topic_visibility"] = from_bool(
            self.can_toggle_topic_visibility)
        result["can_pin_unpin_topic"] = from_bool(self.can_pin_unpin_topic)
        result["can_moderate_category"] = from_bool(self.can_moderate_category)
        result["can_remove_self_id"] = from_int(self.can_remove_self_id)
        result["participants"] = from_list(
            lambda x: to_class(Participant, x), self.participants)
        result["created_by"] = to_class(CreatedBy, self.created_by)
        result["last_poster"] = to_class(CreatedBy, self.last_poster)
        return result


@dataclass
class PostActionsSummary:
    id: int
    can_act: bool

    @staticmethod
    def from_dict(obj: Any) -> 'PostActionsSummary':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        can_act = from_bool(obj.get("can_act"))
        return PostActionsSummary(id, can_act)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["can_act"] = from_bool(self.can_act)
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
class Post:
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: str
    cooked: str
    post_number: int
    post_type: int
    updated_at: str
    reply_count: int
    reply_to_post_number: int
    quote_count: int
    incoming_link_count: int
    reads: int
    readers_count: int
    score: float
    yours: bool
    topic_id: int
    topic_slug: str
    display_username: str
    primary_group_name: str
    flair_name: str
    flair_url: str
    flair_bg_color: str
    flair_color: str
    version: int
    can_edit: bool
    can_delete: bool
    can_recover: bool
    can_see_hidden_post: bool
    can_wiki: bool
    link_counts: List[LinkCount]
    read: bool
    user_title: str
    bookmarked: bool
    actions_summary: List[PostActionsSummary]
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
    reviewable_id: int
    reviewable_score_count: int
    reviewable_score_pending_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        username = from_str(obj.get("username"))
        avatar_template = from_str(obj.get("avatar_template"))
        created_at = from_str(obj.get("created_at"))
        cooked = from_str(obj.get("cooked"))
        post_number = from_int(obj.get("post_number"))
        post_type = from_int(obj.get("post_type"))
        updated_at = from_str(obj.get("updated_at"))
        reply_count = from_int(obj.get("reply_count"))
        reply_to_post_number = from_int(obj.get("reply_to_post_number"))
        quote_count = from_int(obj.get("quote_count"))
        incoming_link_count = from_int(obj.get("incoming_link_count"))
        reads = from_int(obj.get("reads"))
        readers_count = from_int(obj.get("readers_count"))
        score = from_float(obj.get("score"))
        yours = from_bool(obj.get("yours"))
        topic_id = from_int(obj.get("topic_id"))
        topic_slug = from_str(obj.get("topic_slug"))
        display_username = from_str(obj.get("display_username"))
        primary_group_name = from_str(obj.get("primary_group_name"))
        flair_name = from_str(obj.get("flair_name"))
        flair_url = from_str(obj.get("flair_url"))
        flair_bg_color = from_str(obj.get("flair_bg_color"))
        flair_color = from_str(obj.get("flair_color"))
        version = from_int(obj.get("version"))
        can_edit = from_bool(obj.get("can_edit"))
        can_delete = from_bool(obj.get("can_delete"))
        can_recover = from_bool(obj.get("can_recover"))
        can_see_hidden_post = from_bool(obj.get("can_see_hidden_post"))
        can_wiki = from_bool(obj.get("can_wiki"))
        link_counts = from_list(LinkCount.from_dict, obj.get("link_counts"))
        read = from_bool(obj.get("read"))
        user_title = from_str(obj.get("user_title"))
        bookmarked = from_bool(obj.get("bookmarked"))
        actions_summary = from_list(
            PostActionsSummary.from_dict, obj.get("actions_summary"))
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
        reviewable_id = from_int(obj.get("reviewable_id"))
        reviewable_score_count = from_int(obj.get("reviewable_score_count"))
        reviewable_score_pending_count = from_int(
            obj.get("reviewable_score_pending_count"))
        return Post(id, name, username, avatar_template, created_at, cooked, post_number, post_type, updated_at, reply_count, reply_to_post_number, quote_count, incoming_link_count, reads, readers_count, score, yours, topic_id, topic_slug, display_username, primary_group_name, flair_name, flair_url, flair_bg_color, flair_color, version, can_edit, can_delete, can_recover, can_see_hidden_post, can_wiki, link_counts, read, user_title, bookmarked, actions_summary, moderator, admin, staff, user_id, hidden, trust_level, deleted_at, user_deleted, edit_reason, can_view_edit_history, wiki, reviewable_id, reviewable_score_count, reviewable_score_pending_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["username"] = from_str(self.username)
        result["avatar_template"] = from_str(self.avatar_template)
        result["created_at"] = from_str(self.created_at)
        result["cooked"] = from_str(self.cooked)
        result["post_number"] = from_int(self.post_number)
        result["post_type"] = from_int(self.post_type)
        result["updated_at"] = from_str(self.updated_at)
        result["reply_count"] = from_int(self.reply_count)
        result["reply_to_post_number"] = from_int(self.reply_to_post_number)
        result["quote_count"] = from_int(self.quote_count)
        result["incoming_link_count"] = from_int(self.incoming_link_count)
        result["reads"] = from_int(self.reads)
        result["readers_count"] = from_int(self.readers_count)
        result["score"] = from_float(self.score)
        result["yours"] = from_bool(self.yours)
        result["topic_id"] = from_int(self.topic_id)
        result["topic_slug"] = from_str(self.topic_slug)
        result["display_username"] = from_str(self.display_username)
        result["primary_group_name"] = from_str(self.primary_group_name)
        result["flair_name"] = from_str(self.flair_name)
        result["flair_url"] = from_str(self.flair_url)
        result["flair_bg_color"] = from_str(self.flair_bg_color)
        result["flair_color"] = from_str(self.flair_color)
        result["version"] = from_int(self.version)
        result["can_edit"] = from_bool(self.can_edit)
        result["can_delete"] = from_bool(self.can_delete)
        result["can_recover"] = from_bool(self.can_recover)
        result["can_see_hidden_post"] = from_bool(self.can_see_hidden_post)
        result["can_wiki"] = from_bool(self.can_wiki)
        result["link_counts"] = from_list(
            lambda x: to_class(LinkCount, x), self.link_counts)
        result["read"] = from_bool(self.read)
        result["user_title"] = from_str(self.user_title)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["actions_summary"] = from_list(lambda x: to_class(
            PostActionsSummary, x), self.actions_summary)
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
        result["reviewable_id"] = from_int(self.reviewable_id)
        result["reviewable_score_count"] = from_int(
            self.reviewable_score_count)
        result["reviewable_score_pending_count"] = from_int(
            self.reviewable_score_pending_count)
        return result


@dataclass
class PostStream:
    posts: List[Post]
    stream: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'PostStream':
        assert isinstance(obj, dict)
        posts = from_list(Post.from_dict, obj.get("posts"))
        stream = from_list(from_int, obj.get("stream"))
        return PostStream(posts, stream)

    def to_dict(self) -> dict:
        result: dict = {}
        result["posts"] = from_list(lambda x: to_class(Post, x), self.posts)
        result["stream"] = from_list(from_int, self.stream)
        return result


@dataclass
class Poster:
    extras: str
    description: str
    user: CreatedBy

    @staticmethod
    def from_dict(obj: Any) -> 'Poster':
        assert isinstance(obj, dict)
        extras = from_str(obj.get("extras"))
        description = from_str(obj.get("description"))
        user = CreatedBy.from_dict(obj.get("user"))
        return Poster(extras, description, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["extras"] = from_str(self.extras)
        result["description"] = from_str(self.description)
        result["user"] = to_class(CreatedBy, self.user)
        return result


@dataclass
class TagsDescriptions:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'TagsDescriptions':
        assert isinstance(obj, dict)
        return TagsDescriptions()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class SuggestedTopic:
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    image_url: str
    created_at: str
    last_posted_at: str
    bumped: bool
    bumped_at: str
    archetype: str
    unseen: bool
    pinned: bool
    unpinned: str
    excerpt: str
    visible: bool
    closed: bool
    archived: bool
    bookmarked: str
    liked: str
    tags: List[Any]
    tags_descriptions: TagsDescriptions
    like_count: int
    views: int
    category_id: int
    featured_link: str
    posters: List[Poster]

    @staticmethod
    def from_dict(obj: Any) -> 'SuggestedTopic':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        fancy_title = from_str(obj.get("fancy_title"))
        slug = from_str(obj.get("slug"))
        posts_count = from_int(obj.get("posts_count"))
        reply_count = from_int(obj.get("reply_count"))
        highest_post_number = from_int(obj.get("highest_post_number"))
        image_url = from_str(obj.get("image_url"))
        created_at = from_str(obj.get("created_at"))
        last_posted_at = from_str(obj.get("last_posted_at"))
        bumped = from_bool(obj.get("bumped"))
        bumped_at = from_str(obj.get("bumped_at"))
        archetype = from_str(obj.get("archetype"))
        unseen = from_bool(obj.get("unseen"))
        pinned = from_bool(obj.get("pinned"))
        unpinned = from_str(obj.get("unpinned"))
        excerpt = from_str(obj.get("excerpt"))
        visible = from_bool(obj.get("visible"))
        closed = from_bool(obj.get("closed"))
        archived = from_bool(obj.get("archived"))
        bookmarked = from_str(obj.get("bookmarked"))
        liked = from_str(obj.get("liked"))
        tags = from_list(lambda x: x, obj.get("tags"))
        tags_descriptions = TagsDescriptions.from_dict(
            obj.get("tags_descriptions"))
        like_count = from_int(obj.get("like_count"))
        views = from_int(obj.get("views"))
        category_id = from_int(obj.get("category_id"))
        featured_link = from_str(obj.get("featured_link"))
        posters = from_list(Poster.from_dict, obj.get("posters"))
        return SuggestedTopic(id, title, fancy_title, slug, posts_count, reply_count, highest_post_number, image_url, created_at, last_posted_at, bumped, bumped_at, archetype, unseen, pinned, unpinned, excerpt, visible, closed, archived, bookmarked, liked, tags, tags_descriptions, like_count, views, category_id, featured_link, posters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["fancy_title"] = from_str(self.fancy_title)
        result["slug"] = from_str(self.slug)
        result["posts_count"] = from_int(self.posts_count)
        result["reply_count"] = from_int(self.reply_count)
        result["highest_post_number"] = from_int(self.highest_post_number)
        result["image_url"] = from_str(self.image_url)
        result["created_at"] = from_str(self.created_at)
        result["last_posted_at"] = from_str(self.last_posted_at)
        result["bumped"] = from_bool(self.bumped)
        result["bumped_at"] = from_str(self.bumped_at)
        result["archetype"] = from_str(self.archetype)
        result["unseen"] = from_bool(self.unseen)
        result["pinned"] = from_bool(self.pinned)
        result["unpinned"] = from_str(self.unpinned)
        result["excerpt"] = from_str(self.excerpt)
        result["visible"] = from_bool(self.visible)
        result["closed"] = from_bool(self.closed)
        result["archived"] = from_bool(self.archived)
        result["bookmarked"] = from_str(self.bookmarked)
        result["liked"] = from_str(self.liked)
        result["tags"] = from_list(lambda x: x,  self.tags)
        result["tags_descriptions"] = to_class(
            TagsDescriptions, self.tags_descriptions)
        result["like_count"] = from_int(self.like_count)
        result["views"] = from_int(self.views)
        result["category_id"] = from_int(self.category_id)
        result["featured_link"] = from_str(self.featured_link)
        result["posters"] = from_list(
            lambda x: to_class(Poster, x), self.posters)
        return result


@dataclass
class Thumbnail:
    max_width: int
    max_height: int
    width: int
    height: int
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Thumbnail':
        assert isinstance(obj, dict)
        max_width = from_int(obj.get("max_width"))
        max_height = from_int(obj.get("max_height"))
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        url = from_str(obj.get("url"))
        return Thumbnail(max_width, max_height, width, height, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["max_width"] = from_int(self.max_width)
        result["max_height"] = from_int(self.max_height)
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["url"] = from_str(self.url)
        return result


@dataclass
class Topic:
    post_stream: PostStream
    timeline_lookup: List[List[int]]
    suggested_topics: List[SuggestedTopic]
    tags: List[str]
    tags_descriptions: TagsDescriptions
    id: int
    title: str
    fancy_title: str
    posts_count: int
    created_at: str
    views: int
    reply_count: int
    like_count: int
    last_posted_at: str
    visible: bool
    closed: bool
    archived: bool
    has_summary: bool
    archetype: str
    slug: str
    category_id: int
    word_count: int
    deleted_at: str
    user_id: int
    featured_link: str
    pinned_globally: bool
    pinned_at: str
    pinned_until: str
    image_url: str
    slow_mode_seconds: int
    draft: str
    draft_key: str
    draft_sequence: int
    unpinned: str
    pinned: bool
    current_post_number: int
    highest_post_number: int
    deleted_by: str
    has_deleted: bool
    actions_summary: List[TopicActionsSummary]
    chunk_size: int
    bookmarked: bool
    bookmarks: List[Any]
    topic_timer: str
    message_bus_last_id: int
    participant_count: int
    show_read_indicator: bool
    thumbnails: List[Thumbnail]
    slow_mode_enabled_until: str
    summarizable: bool
    details: Details

    @staticmethod
    def from_dict(obj: Any) -> 'Topic':
        assert isinstance(obj, dict)
        post_stream = PostStream.from_dict(obj.get("post_stream"))
        timeline_lookup = from_list(
            lambda x: from_list(from_int, x), obj.get("timeline_lookup"))
        suggested_topics = from_list(
            SuggestedTopic.from_dict, obj.get("suggested_topics"))
        tags = from_list(from_str, obj.get("tags"))
        tags_descriptions = TagsDescriptions.from_dict(
            obj.get("tags_descriptions"))
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        fancy_title = from_str(obj.get("fancy_title"))
        posts_count = from_int(obj.get("posts_count"))
        created_at = from_str(obj.get("created_at"))
        views = from_int(obj.get("views"))
        reply_count = from_int(obj.get("reply_count"))
        like_count = from_int(obj.get("like_count"))
        last_posted_at = from_str(obj.get("last_posted_at"))
        visible = from_bool(obj.get("visible"))
        closed = from_bool(obj.get("closed"))
        archived = from_bool(obj.get("archived"))
        has_summary = from_bool(obj.get("has_summary"))
        archetype = from_str(obj.get("archetype"))
        slug = from_str(obj.get("slug"))
        category_id = from_int(obj.get("category_id"))
        word_count = from_int(obj.get("word_count"))
        deleted_at = from_str(obj.get("deleted_at"))
        user_id = from_int(obj.get("user_id"))
        featured_link = from_str(obj.get("featured_link"))
        pinned_globally = from_bool(obj.get("pinned_globally"))
        pinned_at = from_str(obj.get("pinned_at"))
        pinned_until = from_str(obj.get("pinned_until"))
        image_url = from_str(obj.get("image_url"))
        slow_mode_seconds = from_int(obj.get("slow_mode_seconds"))
        draft = from_str(obj.get("draft"))
        draft_key = from_str(obj.get("draft_key"))
        draft_sequence = from_int(obj.get("draft_sequence"))
        unpinned = from_str(obj.get("unpinned"))
        pinned = from_bool(obj.get("pinned"))
        current_post_number = from_int(obj.get("current_post_number"))
        highest_post_number = from_int(obj.get("highest_post_number"))
        deleted_by = from_str(obj.get("deleted_by"))
        has_deleted = from_bool(obj.get("has_deleted"))
        actions_summary = from_list(
            TopicActionsSummary.from_dict, obj.get("actions_summary"))
        chunk_size = from_int(obj.get("chunk_size"))
        bookmarked = from_bool(obj.get("bookmarked"))
        bookmarks = from_list(lambda x: x, obj.get("bookmarks"))
        topic_timer = from_str(obj.get("topic_timer"))
        message_bus_last_id = from_int(obj.get("message_bus_last_id"))
        participant_count = from_int(obj.get("participant_count"))
        show_read_indicator = from_bool(obj.get("show_read_indicator"))
        thumbnails = from_list(Thumbnail.from_dict, obj.get("thumbnails"))
        slow_mode_enabled_until = from_str(obj.get("slow_mode_enabled_until"))
        summarizable = from_bool(obj.get("summarizable"))
        details = Details.from_dict(obj.get("details"))
        return Topic(post_stream, timeline_lookup, suggested_topics, tags, tags_descriptions, id, title, fancy_title, posts_count, created_at, views, reply_count, like_count, last_posted_at, visible, closed, archived, has_summary, archetype, slug, category_id, word_count, deleted_at, user_id, featured_link, pinned_globally, pinned_at, pinned_until, image_url, slow_mode_seconds, draft, draft_key, draft_sequence, unpinned, pinned, current_post_number, highest_post_number, deleted_by, has_deleted, actions_summary, chunk_size, bookmarked, bookmarks, topic_timer, message_bus_last_id, participant_count, show_read_indicator, thumbnails, slow_mode_enabled_until, summarizable, details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["post_stream"] = to_class(PostStream, self.post_stream)
        result["timeline_lookup"] = from_list(
            lambda x: from_list(from_int, x), self.timeline_lookup)
        result["suggested_topics"] = from_list(
            lambda x: to_class(SuggestedTopic, x), self.suggested_topics)
        result["tags"] = from_list(from_str, self.tags)
        result["tags_descriptions"] = to_class(
            TagsDescriptions, self.tags_descriptions)
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["fancy_title"] = from_str(self.fancy_title)
        result["posts_count"] = from_int(self.posts_count)
        result["created_at"] = from_str(self.created_at)
        result["views"] = from_int(self.views)
        result["reply_count"] = from_int(self.reply_count)
        result["like_count"] = from_int(self.like_count)
        result["last_posted_at"] = from_str(self.last_posted_at)
        result["visible"] = from_bool(self.visible)
        result["closed"] = from_bool(self.closed)
        result["archived"] = from_bool(self.archived)
        result["has_summary"] = from_bool(self.has_summary)
        result["archetype"] = from_str(self.archetype)
        result["slug"] = from_str(self.slug)
        result["category_id"] = from_int(self.category_id)
        result["word_count"] = from_int(self.word_count)
        result["deleted_at"] = from_str(self.deleted_at)
        result["user_id"] = from_int(self.user_id)
        result["featured_link"] = from_str(self.featured_link)
        result["pinned_globally"] = from_bool(self.pinned_globally)
        result["pinned_at"] = from_str(self.pinned_at)
        result["pinned_until"] = from_str(self.pinned_until)
        result["image_url"] = from_str(self.image_url)
        result["slow_mode_seconds"] = from_int(self.slow_mode_seconds)
        result["draft"] = from_str(self.draft)
        result["draft_key"] = from_str(self.draft_key)
        result["draft_sequence"] = from_int(self.draft_sequence)
        result["unpinned"] = from_str(self.unpinned)
        result["pinned"] = from_bool(self.pinned)
        result["current_post_number"] = from_int(self.current_post_number)
        result["highest_post_number"] = from_int(self.highest_post_number)
        result["deleted_by"] = from_str(self.deleted_by)
        result["has_deleted"] = from_bool(self.has_deleted)
        result["actions_summary"] = from_list(lambda x: to_class(
            TopicActionsSummary, x), self.actions_summary)
        result["chunk_size"] = from_int(self.chunk_size)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["bookmarks"] = from_list(lambda x: x, self.bookmarks)
        result["topic_timer"] = from_str(self.topic_timer)
        result["message_bus_last_id"] = from_int(self.message_bus_last_id)
        result["participant_count"] = from_int(self.participant_count)
        result["show_read_indicator"] = from_bool(self.show_read_indicator)
        result["thumbnails"] = from_list(Thumbnail.from_dict, self.thumbnails)
        result["slow_mode_enabled_until"] = from_str(
            self.slow_mode_enabled_until)
        result["summarizable"] = from_bool(self.summarizable)
        result["details"] = to_class(Details, self.details)
        return result


def topic_from_dict(s: Any) -> Topic:
    return Topic.from_dict(s)


def topic_to_dict(x: Topic) -> Any:
    return to_class(Topic, x)