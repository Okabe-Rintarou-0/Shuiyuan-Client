import datetime
from enum import Enum
from typing import Any, List, Optional
from models.common import *
from dataclasses import dataclass, field


class SearchQueryOrder(Enum):
    LATEST = 'latest'
    LIKES = 'likes'
    VIEWS = 'views'
    LATEST_TOPIC = 'latest_topic'
    NONE = ''


class SearchQueryStatus(Enum):
    OPEN = 'open'
    CLOSED = 'closed'
    PUBLIC = 'public'
    ARCHIVED = 'archived'
    NO_REPLIES = 'noreplies'
    SINGLE_USER = 'single_user'
    SOLVED = 'solved'
    UNSOLVED = 'unsolved'
    NONE = ''


class SearchQueryIn(Enum):
    TITLE = 'title'
    LIKES = 'likes'
    PERSONAL = 'personal'
    MESSAGES = 'messages'
    SEEN = 'seen'
    UNSEEN = 'unseen'
    POSTED = 'posted'
    CREATED = 'created'
    WATCHING = 'watching'
    TRACKING = 'tracking'
    BOOKMARKS = 'bookmarks'
    ASSIGNED = 'assigned'
    UNASSIGNED = 'unassigned'
    FIRST = 'first'
    PINNED = 'pinned'
    WIKI = 'wiki'


@dataclass
class SearchQuery():
    term: str = ''
    username: str = ''
    category: str = ''
    tags: List[str] = field(default_factory=lambda: [])
    before: str = ''
    after: str = ''
    order: SearchQueryOrder = SearchQueryOrder.NONE
    status: SearchQueryStatus = SearchQueryStatus.NONE
    in_whats: List[SearchQueryIn] = field(default_factory=lambda: [])


@dataclass
class GroupedSearchResult:
    more_posts: None
    more_users: None
    more_categories: None
    term: str
    search_log_id: int
    more_full_page_results: bool
    can_create_topic: bool
    error: None
    post_ids: List[int]
    user_ids: List[Any]
    category_ids: List[Any]
    tag_ids: List[Any]
    group_ids: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'GroupedSearchResult':
        assert isinstance(obj, dict)
        more_posts = from_none(obj.get("more_posts"))
        more_users = from_none(obj.get("more_users"))
        more_categories = from_none(obj.get("more_categories"))
        term = from_str(obj.get("term"))
        search_log_id = from_int(obj.get("search_log_id"))
        more_full_page_results = from_bool(obj.get("more_full_page_results"))
        can_create_topic = from_bool(obj.get("can_create_topic"))
        error = from_none(obj.get("error"))
        post_ids = from_list(from_int, obj.get("post_ids"))
        user_ids = from_list(lambda x: x, obj.get("user_ids"))
        category_ids = from_list(lambda x: x, obj.get("category_ids"))
        tag_ids = from_list(lambda x: x, obj.get("tag_ids"))
        group_ids = from_list(lambda x: x, obj.get("group_ids"))
        return GroupedSearchResult(more_posts, more_users, more_categories, term, search_log_id, more_full_page_results, can_create_topic, error, post_ids, user_ids, category_ids, tag_ids, group_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["more_posts"] = from_none(self.more_posts)
        result["more_users"] = from_none(self.more_users)
        result["more_categories"] = from_none(self.more_categories)
        result["term"] = from_str(self.term)
        result["search_log_id"] = from_int(self.search_log_id)
        result["more_full_page_results"] = from_bool(self.more_full_page_results)
        result["can_create_topic"] = from_bool(self.can_create_topic)
        result["error"] = from_none(self.error)
        result["post_ids"] = from_list(from_int, self.post_ids)
        result["user_ids"] = from_list(lambda x: x, self.user_ids)
        result["category_ids"] = from_list(lambda x: x, self.category_ids)
        result["tag_ids"] = from_list(lambda x: x, self.tag_ids)
        result["group_ids"] = from_list(lambda x: x, self.group_ids)
        return result


@dataclass
class Post:
    id: int
    name: str
    username: str
    avatar_template: str
    created_at: datetime
    like_count: int
    blurb: str
    post_number: int
    topic_id: int

    def is_full(self) -> bool:
        return not self.blurb.endswith('...')

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        username = from_str(obj.get("username"))
        avatar_template = from_str(obj.get("avatar_template"))
        created_at = from_datetime(obj.get("created_at"))
        like_count = from_int(obj.get("like_count"))
        blurb = from_str(obj.get("blurb"))
        post_number = from_int(obj.get("post_number"))
        topic_id = from_int(obj.get("topic_id"))
        return Post(id, name, username, avatar_template, created_at, like_count, blurb, post_number, topic_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["username"] = from_str(self.username)
        result["avatar_template"] = from_str(self.avatar_template)
        result["created_at"] = self.created_at.isoformat()
        result["like_count"] = from_int(self.like_count)
        result["blurb"] = from_str(self.blurb)
        result["post_number"] = from_int(self.post_number)
        result["topic_id"] = from_int(self.topic_id)
        return result


@dataclass
class Topic:
    id: int
    title: str
    fancy_title: str
    slug: str
    posts_count: int
    reply_count: int
    highest_post_number: int
    created_at: datetime
    last_posted_at: datetime
    bumped: bool
    bumped_at: datetime
    archetype: str
    unseen: bool
    pinned: bool
    unpinned: None
    visible: bool
    closed: bool
    archived: bool
    bookmarked: bool
    liked: bool
    tags: List[str]
    tags_descriptions: Any
    category_id: int
    has_accepted_answer: bool
    last_read_post_number: Optional[int]
    unread: Optional[int]
    new_posts: Optional[int]
    unread_posts: Optional[int]
    notification_level: Optional[int]

    @staticmethod
    def from_dict(obj: Any) -> 'Topic':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        fancy_title = from_str(obj.get("fancy_title"))
        slug = from_str(obj.get("slug"))
        posts_count = from_int(obj.get("posts_count"))
        reply_count = from_int(obj.get("reply_count"))
        highest_post_number = from_int(obj.get("highest_post_number"))
        created_at = from_datetime(obj.get("created_at"))
        last_posted_at = from_datetime(obj.get("last_posted_at"))
        bumped = from_bool(obj.get("bumped"))
        bumped_at = from_datetime(obj.get("bumped_at"))
        archetype = from_str(obj.get("archetype"))
        unseen = from_bool(obj.get("unseen"))
        pinned = from_bool(obj.get("pinned"))
        unpinned = from_none(obj.get("unpinned"))
        visible = from_bool(obj.get("visible"))
        closed = from_bool(obj.get("closed"))
        archived = from_bool(obj.get("archived"))
        bookmarked = from_bool(obj.get("bookmarked"))
        liked = from_bool(obj.get("liked"))
        tags = from_list(from_str, obj.get("tags"))
        tags_descriptions = obj.get("tags_descriptions")
        category_id = from_int(obj.get("category_id"))
        has_accepted_answer = from_bool(obj.get("has_accepted_answer"))
        last_read_post_number = from_int(obj.get("last_read_post_number"))
        unread = from_int( obj.get("unread"))
        new_posts = from_int( obj.get("new_posts"))
        unread_posts = from_int(obj.get("unread_posts"))
        notification_level = from_int(obj.get("notification_level"))
        return Topic(id, title, fancy_title, slug, posts_count, reply_count, highest_post_number, created_at, last_posted_at, bumped, bumped_at, archetype, unseen, pinned, unpinned, visible, closed, archived, bookmarked, liked, tags, tags_descriptions, category_id, has_accepted_answer, last_read_post_number, unread, new_posts, unread_posts, notification_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["fancy_title"] = from_str(self.fancy_title)
        result["slug"] = from_str(self.slug)
        result["posts_count"] = from_int(self.posts_count)
        result["reply_count"] = from_int(self.reply_count)
        result["highest_post_number"] = from_int(self.highest_post_number)
        result["created_at"] = self.created_at.isoformat()
        result["last_posted_at"] = self.last_posted_at.isoformat()
        result["bumped"] = from_bool(self.bumped)
        result["bumped_at"] = self.bumped_at.isoformat()
        result["archetype"] = from_str(self.archetype)
        result["pinned"] = from_bool(self.pinned)
        result["unpinned"] = from_none(self.unpinned)
        result["visible"] = from_bool(self.visible)
        result["closed"] = from_bool(self.closed)
        result["archived"] = from_bool(self.archived)
        result["bookmarked"] = from_bool(self.bookmarked)
        result["liked"] = from_bool(self.liked)
        result["tags"] = from_list(from_str, self.tags)
        result["tags_descriptions"] = self.tags_descriptions,
        result["category_id"] = from_int(self.category_id)
        result["has_accepted_answer"] = from_bool(self.has_accepted_answer)
        result["last_read_post_number"] = from_int(self.last_read_post_number)
        result["unread"] = from_int( self.unread)
        result["new_posts"] = from_int( self.new_posts)
        result["unread_posts"] = from_int(self.unread_posts)
        result["notification_level"] = from_int(self.notification_level)
        return result


@dataclass
class SearchResult:
    posts: List[Post]
    topics: List[Topic]
    users: List[Any]
    categories: List[Any]
    tags: List[Any]
    groups: List[Any]
    grouped_search_result: GroupedSearchResult

    @staticmethod
    def from_dict(obj: Any) -> 'SearchResult':
        assert isinstance(obj, dict)
        posts = from_list(Post.from_dict, obj.get("posts"))
        topics = from_list(Topic.from_dict, obj.get("topics"))
        users = from_list(lambda x: x, obj.get("users"))
        categories = from_list(lambda x: x, obj.get("categories"))
        tags = from_list(lambda x: x, obj.get("tags"))
        groups = from_list(lambda x: x, obj.get("groups"))
        grouped_search_result = GroupedSearchResult.from_dict(
            obj.get("grouped_search_result"))
        return SearchResult(posts, topics, users, categories, tags, groups, grouped_search_result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["posts"] = from_list(lambda x: to_class(Post, x), self.posts)
        result["topics"] = from_list(Topic.from_dict, self.topics)
        result["users"] = from_list(lambda x: x, self.users)
        result["categories"] = from_list(lambda x: x, self.categories)
        result["tags"] = from_list(lambda x: x, self.tags)
        result["groups"] = from_list(lambda x: x, self.groups)
        result["grouped_search_result"] = to_class(
            GroupedSearchResult, self.grouped_search_result)
        return result


def search_result_from_dict(s: Any) -> SearchResult:
    return SearchResult.from_dict(s)


def search_result_to_dict(x: SearchResult) -> Any:
    return to_class(SearchResult, x)
