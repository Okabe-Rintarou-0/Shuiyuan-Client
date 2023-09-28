from constants import base_url
from typing import List
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Optional
from models.common import *
from dataclasses import dataclass


@dataclass
class BadgeType:
    id: int
    name: str
    sort_order: int

    @staticmethod
    def from_dict(obj: Any) -> 'BadgeType':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        sort_order = from_int(obj.get("sort_order"))
        return BadgeType(id, name, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["sort_order"] = from_int(self.sort_order)
        return result


@dataclass
class Badge:
    id: int
    name: str
    description: str
    grant_count: int
    allow_title: bool
    multiple_grant: bool
    icon: str
    image_url: None
    listable: bool
    enabled: bool
    badge_grouping_id: int
    system: bool
    slug: str
    manually_grantable: bool
    badge_type_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Badge':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        grant_count = from_int(obj.get("grant_count"))
        allow_title = from_bool(obj.get("allow_title"))
        multiple_grant = from_bool(obj.get("multiple_grant"))
        icon = from_str(obj.get("icon"))
        image_url = from_none(obj.get("image_url"))
        listable = from_bool(obj.get("listable"))
        enabled = from_bool(obj.get("enabled"))
        badge_grouping_id = from_int(obj.get("badge_grouping_id"))
        system = from_bool(obj.get("system"))
        slug = from_str(obj.get("slug"))
        manually_grantable = from_bool(obj.get("manually_grantable"))
        badge_type_id = from_int(obj.get("badge_type_id"))
        return Badge(id, name, description, grant_count, allow_title, multiple_grant, icon, image_url, listable, enabled, badge_grouping_id, system, slug, manually_grantable, badge_type_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["grant_count"] = from_int(self.grant_count)
        result["allow_title"] = from_bool(self.allow_title)
        result["multiple_grant"] = from_bool(self.multiple_grant)
        result["icon"] = from_str(self.icon)
        result["image_url"] = from_none(self.image_url)
        result["listable"] = from_bool(self.listable)
        result["enabled"] = from_bool(self.enabled)
        result["badge_grouping_id"] = from_int(self.badge_grouping_id)
        result["system"] = from_bool(self.system)
        result["slug"] = from_str(self.slug)
        result["manually_grantable"] = from_bool(self.manually_grantable)
        result["badge_type_id"] = from_int(self.badge_type_id)
        return result


@dataclass
class GrantedBy:
    id: int
    username: str
    name: str
    avatar_template: str
    admin: bool
    moderator: bool
    trust_level: int

    @staticmethod
    def from_dict(obj: Any) -> 'GrantedBy':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        admin = from_bool(obj.get("admin"))
        moderator = from_bool(obj.get("moderator"))
        trust_level = from_int(obj.get("trust_level"))
        return GrantedBy(id, username, name, avatar_template, admin, moderator, trust_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        result["admin"] = from_bool(self.admin)
        result["moderator"] = from_bool(self.moderator)
        result["trust_level"] = from_int(self.trust_level)
        return result


@dataclass
class UserBadge:
    id: int
    granted_at: datetime
    grouping_position: int
    post_number: Optional[int]
    topic_id: Optional[int]
    topic_title: Optional[str]
    is_favorite: None
    can_favorite: bool
    badge_id: int
    granted_by_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserBadge':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        granted_at = from_datetime(obj.get("granted_at"))
        grouping_position = from_int(obj.get("grouping_position"))
        post_number = from_union([from_int, from_none], obj.get("post_number"))
        topic_id = from_union([from_int, from_none], obj.get("topic_id"))
        topic_title = from_union([from_str, from_none], obj.get("topic_title"))
        is_favorite = from_none(obj.get("is_favorite"))
        can_favorite = from_bool(obj.get("can_favorite"))
        badge_id = from_int(obj.get("badge_id"))
        granted_by_id = from_int(obj.get("granted_by_id"))
        return UserBadge(id, granted_at, grouping_position, post_number, topic_id, topic_title, is_favorite, can_favorite, badge_id, granted_by_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["granted_at"] = self.granted_at.isoformat()
        result["grouping_position"] = from_int(self.grouping_position)
        result["post_number"] = from_union(
            [from_int, from_none], self.post_number)
        result["topic_id"] = from_union([from_int, from_none], self.topic_id)
        result["topic_title"] = from_union(
            [from_str, from_none], self.topic_title)
        result["is_favorite"] = from_none(self.is_favorite)
        result["can_favorite"] = from_bool(self.can_favorite)
        result["badge_id"] = from_int(self.badge_id)
        result["granted_by_id"] = from_int(self.granted_by_id)
        return result


@dataclass
class UserBadgesInfo:
    badges: List[Badge]
    badge_types: List[BadgeType]
    granted_bies: List[GrantedBy]
    user_badges: List[UserBadge]

    @staticmethod
    def from_dict(obj: Any) -> 'UserBadgesInfo':
        assert isinstance(obj, dict)
        badges = from_list(Badge.from_dict, obj.get("badges"))
        badge_types = from_list(BadgeType.from_dict, obj.get("badge_types"))
        granted_bies = from_list(GrantedBy.from_dict, obj.get("granted_bies"))
        user_badges = from_list(UserBadge.from_dict, obj.get("user_badges"))
        return UserBadgesInfo(badges, badge_types, granted_bies, user_badges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["badges"] = from_list(lambda x: to_class(Badge, x), self.badges)
        result["badge_types"] = from_list(
            lambda x: to_class(BadgeType, x), self.badge_types)
        result["granted_bies"] = from_list(
            lambda x: to_class(GrantedBy, x), self.granted_bies)
        result["user_badges"] = from_list(
            lambda x: to_class(UserBadge, x), self.user_badges)
        return result


def user_badges_info_from_dict(s: Any) -> UserBadgesInfo:
    return UserBadgesInfo.from_dict(s)


def user_badges_info_to_dict(x: UserBadgesInfo) -> Any:
    return to_class(UserBadgesInfo, x)


@dataclass
class AssociatedAccount:
    name: str
    description: str

    @staticmethod
    def from_dict(obj: Any) -> 'AssociatedAccount':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        return AssociatedAccount(name, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        return result


@dataclass
class CustomFields:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'CustomFields':
        assert isinstance(obj, dict)
        return CustomFields()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class GroupUser:
    group_id: int
    user_id: int
    notification_level: int
    owner: bool

    @staticmethod
    def from_dict(obj: Any) -> 'GroupUser':
        assert isinstance(obj, dict)
        group_id = from_int(obj.get("group_id"))
        user_id = from_int(obj.get("user_id"))
        notification_level = from_int(obj.get("notification_level"))
        owner = from_bool(obj.get("owner"))
        return GroupUser(group_id, user_id, notification_level, owner)

    def to_dict(self) -> dict:
        result: dict = {}
        result["group_id"] = from_int(self.group_id)
        result["user_id"] = from_int(self.user_id)
        result["notification_level"] = from_int(self.notification_level)
        result["owner"] = from_bool(self.owner)
        return result


@dataclass
class Group:
    id: int
    automatic: bool
    name: str
    display_name: str
    user_count: int
    mentionable_level: int
    messageable_level: int
    visibility_level: int
    primary_group: bool
    title: None
    grant_trust_level: None
    has_messages: bool
    flair_url: None
    flair_bg_color: Optional[str]
    flair_color: Optional[str]
    bio_cooked: None
    bio_excerpt: None
    public_admission: bool
    public_exit: bool
    allow_membership_requests: bool
    full_name: None
    default_notification_level: int
    membership_request_template: None
    members_visibility_level: int
    can_see_members: bool
    publish_read_state: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        automatic = from_bool(obj.get("automatic"))
        name = from_str(obj.get("name"))
        display_name = from_str(obj.get("display_name"))
        user_count = from_int(obj.get("user_count"))
        mentionable_level = from_int(obj.get("mentionable_level"))
        messageable_level = from_int(obj.get("messageable_level"))
        visibility_level = from_int(obj.get("visibility_level"))
        primary_group = from_bool(obj.get("primary_group"))
        title = from_none(obj.get("title"))
        grant_trust_level = from_none(obj.get("grant_trust_level"))
        has_messages = from_bool(obj.get("has_messages"))
        flair_url = from_none(obj.get("flair_url"))
        flair_bg_color = from_union(
            [from_str, from_none], obj.get("flair_bg_color"))
        flair_color = from_union([from_str, from_none], obj.get("flair_color"))
        bio_cooked = from_none(obj.get("bio_cooked"))
        bio_excerpt = from_none(obj.get("bio_excerpt"))
        public_admission = from_bool(obj.get("public_admission"))
        public_exit = from_bool(obj.get("public_exit"))
        allow_membership_requests = from_bool(
            obj.get("allow_membership_requests"))
        full_name = from_none(obj.get("full_name"))
        default_notification_level = from_int(
            obj.get("default_notification_level"))
        membership_request_template = from_none(
            obj.get("membership_request_template"))
        members_visibility_level = from_int(
            obj.get("members_visibility_level"))
        can_see_members = from_bool(obj.get("can_see_members"))
        publish_read_state = from_bool(obj.get("publish_read_state"))
        return Group(id, automatic, name, display_name, user_count, mentionable_level, messageable_level, visibility_level, primary_group, title, grant_trust_level, has_messages, flair_url, flair_bg_color, flair_color, bio_cooked, bio_excerpt, public_admission, public_exit, allow_membership_requests, full_name, default_notification_level, membership_request_template, members_visibility_level, can_see_members, publish_read_state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["automatic"] = from_bool(self.automatic)
        result["name"] = from_str(self.name)
        result["display_name"] = from_str(self.display_name)
        result["user_count"] = from_int(self.user_count)
        result["mentionable_level"] = from_int(self.mentionable_level)
        result["messageable_level"] = from_int(self.messageable_level)
        result["visibility_level"] = from_int(self.visibility_level)
        result["primary_group"] = from_bool(self.primary_group)
        result["title"] = from_none(self.title)
        result["grant_trust_level"] = from_none(self.grant_trust_level)
        result["has_messages"] = from_bool(self.has_messages)
        result["flair_url"] = from_none(self.flair_url)
        result["flair_bg_color"] = from_union(
            [from_str, from_none], self.flair_bg_color)
        result["flair_color"] = from_union(
            [from_str, from_none], self.flair_color)
        result["bio_cooked"] = from_none(self.bio_cooked)
        result["bio_excerpt"] = from_none(self.bio_excerpt)
        result["public_admission"] = from_bool(self.public_admission)
        result["public_exit"] = from_bool(self.public_exit)
        result["allow_membership_requests"] = from_bool(
            self.allow_membership_requests)
        result["full_name"] = from_none(self.full_name)
        result["default_notification_level"] = from_int(
            self.default_notification_level)
        result["membership_request_template"] = from_none(
            self.membership_request_template)
        result["members_visibility_level"] = from_int(
            self.members_visibility_level)
        result["can_see_members"] = from_bool(self.can_see_members)
        result["publish_read_state"] = from_bool(self.publish_read_state)
        return result


@dataclass
class SidebarTag:
    name: str
    description: None
    pm_only: bool

    @staticmethod
    def from_dict(obj: Any) -> 'SidebarTag':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_none(obj.get("description"))
        pm_only = from_bool(obj.get("pm_only"))
        return SidebarTag(name, description, pm_only)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_none(self.description)
        result["pm_only"] = from_bool(self.pm_only)
        return result


@dataclass
class UserAPIKey:
    id: int
    application_name: str
    scopes: List[str]
    created_at: datetime
    last_used_at: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'UserAPIKey':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        application_name = from_str(obj.get("application_name"))
        scopes = from_list(from_str, obj.get("scopes"))
        created_at = from_datetime(obj.get("created_at"))
        last_used_at = from_datetime(obj.get("last_used_at"))
        return UserAPIKey(id, application_name, scopes, created_at, last_used_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["application_name"] = from_str(self.application_name)
        result["scopes"] = from_list(from_str, self.scopes)
        result["created_at"] = self.created_at.isoformat()
        result["last_used_at"] = self.last_used_at.isoformat()
        return result


@dataclass
class UserAuthToken:
    id: int
    client_ip: str
    location: str
    browser: str
    device: str
    os: str
    icon: str
    created_at: datetime
    seen_at: datetime
    is_active: bool

    @staticmethod
    def from_dict(obj: Any) -> 'UserAuthToken':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        client_ip = from_str(obj.get("client_ip"))
        location = from_str(obj.get("location"))
        browser = from_str(obj.get("browser"))
        device = from_str(obj.get("device"))
        os = from_str(obj.get("os"))
        icon = from_str(obj.get("icon"))
        created_at = from_datetime(obj.get("created_at"))
        seen_at = from_datetime(obj.get("seen_at"))
        is_active = from_bool(obj.get("is_active"))
        return UserAuthToken(id, client_ip, location, browser, device, os, icon, created_at, seen_at, is_active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["client_ip"] = from_str(self.client_ip)
        result["location"] = from_str(self.location)
        result["browser"] = from_str(self.browser)
        result["device"] = from_str(self.device)
        result["os"] = from_str(self.os)
        result["icon"] = from_str(self.icon)
        result["created_at"] = self.created_at.isoformat()
        result["seen_at"] = self.seen_at.isoformat()
        result["is_active"] = from_bool(self.is_active)
        return result


@dataclass
class UserNotificationSchedule:
    enabled: bool
    day_0__start_time: int
    day_0__end_time: int
    day_1__start_time: int
    day_1__end_time: int
    day_2__start_time: int
    day_2__end_time: int
    day_3__start_time: int
    day_3__end_time: int
    day_4__start_time: int
    day_4__end_time: int
    day_5__start_time: int
    day_5__end_time: int
    day_6__start_time: int
    day_6__end_time: int

    @staticmethod
    def from_dict(obj: Any) -> 'UserNotificationSchedule':
        assert isinstance(obj, dict)
        enabled = from_bool(obj.get("enabled"))
        day_0__start_time = from_int(obj.get("day_0_start_time"))
        day_0__end_time = from_int(obj.get("day_0_end_time"))
        day_1__start_time = from_int(obj.get("day_1_start_time"))
        day_1__end_time = from_int(obj.get("day_1_end_time"))
        day_2__start_time = from_int(obj.get("day_2_start_time"))
        day_2__end_time = from_int(obj.get("day_2_end_time"))
        day_3__start_time = from_int(obj.get("day_3_start_time"))
        day_3__end_time = from_int(obj.get("day_3_end_time"))
        day_4__start_time = from_int(obj.get("day_4_start_time"))
        day_4__end_time = from_int(obj.get("day_4_end_time"))
        day_5__start_time = from_int(obj.get("day_5_start_time"))
        day_5__end_time = from_int(obj.get("day_5_end_time"))
        day_6__start_time = from_int(obj.get("day_6_start_time"))
        day_6__end_time = from_int(obj.get("day_6_end_time"))
        return UserNotificationSchedule(enabled, day_0__start_time, day_0__end_time, day_1__start_time, day_1__end_time, day_2__start_time, day_2__end_time, day_3__start_time, day_3__end_time, day_4__start_time, day_4__end_time, day_5__start_time, day_5__end_time, day_6__start_time, day_6__end_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_bool(self.enabled)
        result["day_0_start_time"] = from_int(self.day_0__start_time)
        result["day_0_end_time"] = from_int(self.day_0__end_time)
        result["day_1_start_time"] = from_int(self.day_1__start_time)
        result["day_1_end_time"] = from_int(self.day_1__end_time)
        result["day_2_start_time"] = from_int(self.day_2__start_time)
        result["day_2_end_time"] = from_int(self.day_2__end_time)
        result["day_3_start_time"] = from_int(self.day_3__start_time)
        result["day_3_end_time"] = from_int(self.day_3__end_time)
        result["day_4_start_time"] = from_int(self.day_4__start_time)
        result["day_4_end_time"] = from_int(self.day_4__end_time)
        result["day_5_start_time"] = from_int(self.day_5__start_time)
        result["day_5_end_time"] = from_int(self.day_5__end_time)
        result["day_6_start_time"] = from_int(self.day_6__start_time)
        result["day_6_end_time"] = from_int(self.day_6__end_time)
        return result


@dataclass
class UserOption:
    user_id: int
    mailing_list_mode: bool
    mailing_list_mode_frequency: int
    email_digests: bool
    email_level: int
    email_messages_level: int
    external_links_in_new_tab: bool
    color_scheme_id: None
    dark_scheme_id: None
    dynamic_favicon: bool
    enable_quoting: bool
    enable_defer: bool
    digest_after_minutes: None
    automatically_unpin_topics: bool
    auto_track_topics_after_msecs: int
    notification_level_when_replying: int
    new_topic_duration_minutes: int
    email_previous_replies: int
    email_in_reply_to: bool
    like_notification_frequency: int
    include_tl0_in_digests: bool
    theme_ids: List[int]
    theme_key_seq: int
    allow_private_messages: bool
    enable_allowed_pm_users: bool
    homepage_id: None
    hide_profile_and_presence: bool
    text_size: str
    text_size_seq: int
    title_count_mode: str
    bookmark_auto_delete_preference: int
    timezone: str
    skip_new_user_tips: bool
    default_calendar: str
    oldest_search_log_date: None
    seen_popups: List[int]
    sidebar_link_to_filtered_list: bool
    sidebar_show_count_of_new_items: bool
    watched_precedence_over_muted: None

    @staticmethod
    def from_dict(obj: Any) -> 'UserOption':
        assert isinstance(obj, dict)
        user_id = from_int(obj.get("user_id"))
        mailing_list_mode = from_bool(obj.get("mailing_list_mode"))
        mailing_list_mode_frequency = from_int(
            obj.get("mailing_list_mode_frequency"))
        email_digests = from_bool(obj.get("email_digests"))
        email_level = from_int(obj.get("email_level"))
        email_messages_level = from_int(obj.get("email_messages_level"))
        external_links_in_new_tab = from_bool(
            obj.get("external_links_in_new_tab"))
        color_scheme_id = from_none(obj.get("color_scheme_id"))
        dark_scheme_id = from_none(obj.get("dark_scheme_id"))
        dynamic_favicon = from_bool(obj.get("dynamic_favicon"))
        enable_quoting = from_bool(obj.get("enable_quoting"))
        enable_defer = from_bool(obj.get("enable_defer"))
        digest_after_minutes = from_none(obj.get("digest_after_minutes"))
        automatically_unpin_topics = from_bool(
            obj.get("automatically_unpin_topics"))
        auto_track_topics_after_msecs = from_int(
            obj.get("auto_track_topics_after_msecs"))
        notification_level_when_replying = from_int(
            obj.get("notification_level_when_replying"))
        new_topic_duration_minutes = from_int(
            obj.get("new_topic_duration_minutes"))
        email_previous_replies = from_int(obj.get("email_previous_replies"))
        email_in_reply_to = from_bool(obj.get("email_in_reply_to"))
        like_notification_frequency = from_int(
            obj.get("like_notification_frequency"))
        include_tl0_in_digests = from_bool(obj.get("include_tl0_in_digests"))
        theme_ids = from_list(from_int, obj.get("theme_ids"))
        theme_key_seq = from_int(obj.get("theme_key_seq"))
        allow_private_messages = from_bool(obj.get("allow_private_messages"))
        enable_allowed_pm_users = from_bool(obj.get("enable_allowed_pm_users"))
        homepage_id = from_none(obj.get("homepage_id"))
        hide_profile_and_presence = from_bool(
            obj.get("hide_profile_and_presence"))
        text_size = from_str(obj.get("text_size"))
        text_size_seq = from_int(obj.get("text_size_seq"))
        title_count_mode = from_str(obj.get("title_count_mode"))
        bookmark_auto_delete_preference = from_int(
            obj.get("bookmark_auto_delete_preference"))
        timezone = from_str(obj.get("timezone"))
        skip_new_user_tips = from_bool(obj.get("skip_new_user_tips"))
        default_calendar = from_str(obj.get("default_calendar"))
        oldest_search_log_date = from_none(obj.get("oldest_search_log_date"))
        seen_popups = from_list(from_int, obj.get("seen_popups"))
        sidebar_link_to_filtered_list = from_bool(
            obj.get("sidebar_link_to_filtered_list"))
        sidebar_show_count_of_new_items = from_bool(
            obj.get("sidebar_show_count_of_new_items"))
        watched_precedence_over_muted = from_none(
            obj.get("watched_precedence_over_muted"))
        return UserOption(user_id, mailing_list_mode, mailing_list_mode_frequency, email_digests, email_level, email_messages_level, external_links_in_new_tab, color_scheme_id, dark_scheme_id, dynamic_favicon, enable_quoting, enable_defer, digest_after_minutes, automatically_unpin_topics, auto_track_topics_after_msecs, notification_level_when_replying, new_topic_duration_minutes, email_previous_replies, email_in_reply_to, like_notification_frequency, include_tl0_in_digests, theme_ids, theme_key_seq, allow_private_messages, enable_allowed_pm_users, homepage_id, hide_profile_and_presence, text_size, text_size_seq, title_count_mode, bookmark_auto_delete_preference, timezone, skip_new_user_tips, default_calendar, oldest_search_log_date, seen_popups, sidebar_link_to_filtered_list, sidebar_show_count_of_new_items, watched_precedence_over_muted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_int(self.user_id)
        result["mailing_list_mode"] = from_bool(self.mailing_list_mode)
        result["mailing_list_mode_frequency"] = from_int(
            self.mailing_list_mode_frequency)
        result["email_digests"] = from_bool(self.email_digests)
        result["email_level"] = from_int(self.email_level)
        result["email_messages_level"] = from_int(self.email_messages_level)
        result["external_links_in_new_tab"] = from_bool(
            self.external_links_in_new_tab)
        result["color_scheme_id"] = from_none(self.color_scheme_id)
        result["dark_scheme_id"] = from_none(self.dark_scheme_id)
        result["dynamic_favicon"] = from_bool(self.dynamic_favicon)
        result["enable_quoting"] = from_bool(self.enable_quoting)
        result["enable_defer"] = from_bool(self.enable_defer)
        result["digest_after_minutes"] = from_none(self.digest_after_minutes)
        result["automatically_unpin_topics"] = from_bool(
            self.automatically_unpin_topics)
        result["auto_track_topics_after_msecs"] = from_int(
            self.auto_track_topics_after_msecs)
        result["notification_level_when_replying"] = from_int(
            self.notification_level_when_replying)
        result["new_topic_duration_minutes"] = from_int(
            self.new_topic_duration_minutes)
        result["email_previous_replies"] = from_int(
            self.email_previous_replies)
        result["email_in_reply_to"] = from_bool(self.email_in_reply_to)
        result["like_notification_frequency"] = from_int(
            self.like_notification_frequency)
        result["include_tl0_in_digests"] = from_bool(
            self.include_tl0_in_digests)
        result["theme_ids"] = from_list(from_int, self.theme_ids)
        result["theme_key_seq"] = from_int(self.theme_key_seq)
        result["allow_private_messages"] = from_bool(
            self.allow_private_messages)
        result["enable_allowed_pm_users"] = from_bool(
            self.enable_allowed_pm_users)
        result["homepage_id"] = from_none(self.homepage_id)
        result["hide_profile_and_presence"] = from_bool(
            self.hide_profile_and_presence)
        result["text_size"] = from_str(self.text_size)
        result["text_size_seq"] = from_int(self.text_size_seq)
        result["title_count_mode"] = from_str(self.title_count_mode)
        result["bookmark_auto_delete_preference"] = from_int(
            self.bookmark_auto_delete_preference)
        result["timezone"] = from_str(self.timezone)
        result["skip_new_user_tips"] = from_bool(self.skip_new_user_tips)
        result["default_calendar"] = from_str(self.default_calendar)
        result["oldest_search_log_date"] = from_none(
            self.oldest_search_log_date)
        result["seen_popups"] = from_list(from_int, self.seen_popups)
        result["sidebar_link_to_filtered_list"] = from_bool(
            self.sidebar_link_to_filtered_list)
        result["sidebar_show_count_of_new_items"] = from_bool(
            self.sidebar_show_count_of_new_items)
        result["watched_precedence_over_muted"] = from_none(
            self.watched_precedence_over_muted)
        return result


@dataclass
class User:
    id: int
    username: str
    name: str
    avatar_template: str
    email: Optional[str]
    secondary_emails: List[Any]
    unconfirmed_emails: List[Any]
    last_posted_at: datetime
    last_seen_at: datetime
    created_at: datetime
    ignored: bool
    muted: bool
    can_ignore_user: bool
    can_mute_user: bool
    can_send_private_messages: bool
    can_send_private_message_to_user: bool
    trust_level: int
    moderator: bool
    admin: bool
    title: str
    badge_count: int
    custom_fields: CustomFields
    time_read: int
    recent_time_read: int
    primary_group_id: None
    primary_group_name: None
    flair_group_id: None
    flair_name: None
    flair_url: None
    flair_bg_color: None
    flair_color: None
    featured_topic: None
    timezone: str
    pending_posts_count: int
    can_edit: bool
    can_edit_username: bool
    can_edit_email: bool
    can_edit_name: bool
    uploaded_avatar_id: Optional[int]
    has_title_badges: Optional[bool]
    pending_count: int
    profile_view_count: int
    second_factor_enabled: Optional[bool]
    second_factor_backup_enabled: Optional[bool]
    associated_accounts: List[AssociatedAccount]
    can_upload_profile_header: bool
    can_upload_user_card_background: bool
    locale: Optional[str]
    muted_category_ids: List[int]
    regular_category_ids: List[Any]
    watched_tags: List[Any]
    watching_first_post_tags: List[Any]
    tracked_tags: List[Any]
    muted_tags: List[Any]
    tracked_category_ids: List[Any]
    watched_category_ids: List[Any]
    watched_first_post_category_ids: List[int]
    system_avatar_upload_id: None
    system_avatar_template: Optional[str]
    custom_avatar_upload_id: int
    custom_avatar_template: str
    muted_usernames: List[Any]
    ignored_usernames: List[Any]
    allowed_pm_usernames: List[Any]
    mailing_list_posts_per_day: Optional[int]
    can_change_bio: Optional[bool]
    can_change_location: Optional[bool]
    can_change_website: Optional[bool]
    can_change_tracking_preferences: Optional[bool]
    user_api_keys: List[UserAPIKey]
    user_auth_tokens: List[UserAuthToken]
    user_notification_schedule: Optional[UserNotificationSchedule]
    use_logo_small_as_avatar: Optional[bool]
    sidebar_tags: List[SidebarTag]
    sidebar_category_ids: List[int]
    display_sidebar_tags: Optional[bool]
    cakedate: datetime
    birthdate: None
    accepted_answers: int
    featured_user_badge_ids: List[int]
    invited_by: None
    groups: List[Group]
    group_users: List[GroupUser]
    user_option: Optional[UserOption]

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = from_str(obj.get("username"))
        name = from_str(obj.get("name"))
        avatar_template = from_str(obj.get("avatar_template"))
        email = from_union([from_str, from_none], obj.get("email"))
        secondary_emails = from_union([lambda x: from_list(
            lambda x: x, x), from_none], obj.get("secondary_emails"))
        unconfirmed_emails = from_union([lambda x: from_list(
            lambda x: x, x), from_none], obj.get("unconfirmed_emails"))
        last_posted_at = from_datetime(obj.get("last_posted_at"))
        last_seen_at = from_datetime(obj.get("last_seen_at"))
        created_at = from_datetime(obj.get("created_at"))
        ignored = from_bool(obj.get("ignored"))
        muted = from_bool(obj.get("muted"))
        can_ignore_user = from_bool(obj.get("can_ignore_user"))
        can_mute_user = from_bool(obj.get("can_mute_user"))
        can_send_private_messages = from_bool(
            obj.get("can_send_private_messages"))
        can_send_private_message_to_user = from_bool(
            obj.get("can_send_private_message_to_user"))
        trust_level = from_int(obj.get("trust_level"))
        moderator = from_bool(obj.get("moderator"))
        admin = from_bool(obj.get("admin"))
        title = from_str(obj.get("title"))
        badge_count = from_int(obj.get("badge_count"))
        custom_fields = CustomFields.from_dict(obj.get("custom_fields"))
        time_read = from_int(obj.get("time_read"))
        recent_time_read = from_int(obj.get("recent_time_read"))
        primary_group_id = from_none(obj.get("primary_group_id"))
        primary_group_name = from_none(obj.get("primary_group_name"))
        flair_group_id = from_none(obj.get("flair_group_id"))
        flair_name = from_none(obj.get("flair_name"))
        flair_url = from_none(obj.get("flair_url"))
        flair_bg_color = from_none(obj.get("flair_bg_color"))
        flair_color = from_none(obj.get("flair_color"))
        featured_topic = from_none(obj.get("featured_topic"))
        timezone = from_str(obj.get("timezone"))
        pending_posts_count = from_union(
            [from_int, from_none], obj.get("pending_posts_count"))
        can_edit = from_bool(obj.get("can_edit"))
        can_edit_username = from_bool(obj.get("can_edit_username"))
        can_edit_email = from_bool(obj.get("can_edit_email"))
        can_edit_name = from_bool(obj.get("can_edit_name"))
        uploaded_avatar_id = from_union(
            [from_int, from_none], obj.get("uploaded_avatar_id"))
        has_title_badges = from_union(
            [from_bool, from_none], obj.get("has_title_badges"))
        pending_count = from_int(obj.get("pending_count"))
        profile_view_count = from_int(obj.get("profile_view_count"))
        second_factor_enabled = from_union(
            [from_bool, from_none], obj.get("second_factor_enabled"))
        second_factor_backup_enabled = from_union(
            [from_bool, from_none], obj.get("second_factor_backup_enabled"))
        associated_accounts = from_list(
            AssociatedAccount.from_dict, obj.get("associated_accounts"))
        can_upload_profile_header = from_bool(
            obj.get("can_upload_profile_header"))
        can_upload_user_card_background = from_bool(
            obj.get("can_upload_user_card_background"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        muted_category_ids = from_list(from_int, obj.get("muted_category_ids"))
        regular_category_ids = from_list(
            lambda x: x, obj.get("regular_category_ids"))
        watched_tags = from_list(lambda x: x, obj.get("watched_tags"))
        watching_first_post_tags = from_list(
            lambda x: x, obj.get("watching_first_post_tags"))
        tracked_tags = from_list(lambda x: x, obj.get("tracked_tags"))
        muted_tags = from_list(lambda x: x, obj.get("muted_tags"))
        tracked_category_ids = from_list(
            lambda x: x, obj.get("tracked_category_ids"))
        watched_category_ids = from_list(
            lambda x: x, obj.get("watched_category_ids"))
        watched_first_post_category_ids = from_list(
            from_int, obj.get("watched_first_post_category_ids"))
        system_avatar_upload_id = from_none(obj.get("system_avatar_upload_id"))
        system_avatar_template = from_union(
            [from_str, from_none], obj.get("system_avatar_template"))
        custom_avatar_upload_id = from_int(obj.get("custom_avatar_upload_id"))
        custom_avatar_template = from_str(obj.get("custom_avatar_template"))
        muted_usernames = from_list(lambda x: x, obj.get("muted_usernames"))
        ignored_usernames = from_list(
            lambda x: x, obj.get("ignored_usernames"))
        allowed_pm_usernames = from_list(
            lambda x: x, obj.get("allowed_pm_usernames"))
        mailing_list_posts_per_day = from_union(
            [from_int, from_none], obj.get("mailing_list_posts_per_day"))
        can_change_bio = from_union(
            [from_bool, from_none], obj.get("can_change_bio"))
        can_change_location = from_union(
            [from_bool, from_none], obj.get("can_change_location"))
        can_change_website = from_union(
            [from_bool, from_none], obj.get("can_change_website"))
        can_change_tracking_preferences = from_union(
            [from_bool, from_none], obj.get("can_change_tracking_preferences"))
        user_api_keys = from_list(
            UserAPIKey.from_dict, obj.get("user_api_keys"))
        user_auth_tokens = from_list(
            UserAuthToken.from_dict, obj.get("user_auth_tokens"))
        user_notification_schedule = from_union(
            [from_none, UserNotificationSchedule.from_dict], obj.get("user_notification_schedule"))
        use_logo_small_as_avatar = from_union(
            [from_bool, from_none], obj.get("use_logo_small_as_avatar"))
        sidebar_tags = from_list(SidebarTag.from_dict, obj.get("sidebar_tags"))
        sidebar_category_ids = from_list(
            from_int, obj.get("sidebar_category_ids"))
        display_sidebar_tags = from_union(
            [from_bool, from_none], obj.get("display_sidebar_tags"))
        cakedate = from_datetime(obj.get("cakedate"))
        birthdate = from_none(obj.get("birthdate"))
        accepted_answers = from_int(obj.get("accepted_answers"))
        featured_user_badge_ids = from_list(
            from_int, obj.get("featured_user_badge_ids"))
        invited_by = from_none(obj.get("invited_by"))
        groups = from_list(Group.from_dict, obj.get("groups"))
        group_users = from_list(GroupUser.from_dict, obj.get("group_users"))
        user_option = from_union(
            [UserOption.from_dict, from_none], obj.get("user_option"))
        return User(id, username, name, avatar_template, email, secondary_emails, unconfirmed_emails, last_posted_at, last_seen_at, created_at, ignored, muted, can_ignore_user, can_mute_user, can_send_private_messages, can_send_private_message_to_user, trust_level, moderator, admin, title, badge_count, custom_fields, time_read, recent_time_read, primary_group_id, primary_group_name, flair_group_id, flair_name, flair_url, flair_bg_color, flair_color, featured_topic, timezone, pending_posts_count, can_edit, can_edit_username, can_edit_email, can_edit_name, uploaded_avatar_id, has_title_badges, pending_count, profile_view_count, second_factor_enabled, second_factor_backup_enabled, associated_accounts, can_upload_profile_header, can_upload_user_card_background, locale, muted_category_ids, regular_category_ids, watched_tags, watching_first_post_tags, tracked_tags, muted_tags, tracked_category_ids, watched_category_ids, watched_first_post_category_ids, system_avatar_upload_id, system_avatar_template, custom_avatar_upload_id, custom_avatar_template, muted_usernames, ignored_usernames, allowed_pm_usernames, mailing_list_posts_per_day, can_change_bio, can_change_location, can_change_website, can_change_tracking_preferences, user_api_keys, user_auth_tokens, user_notification_schedule, use_logo_small_as_avatar, sidebar_tags, sidebar_category_ids, display_sidebar_tags, cakedate, birthdate, accepted_answers, featured_user_badge_ids, invited_by, groups, group_users, user_option)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = from_str(self.username)
        result["name"] = from_str(self.name)
        result["avatar_template"] = from_str(self.avatar_template)
        result["email"] = from_union([from_str, from_none], self.email)
        result["secondary_emails"] = from_union([lambda x: from_list(
            lambda x: x, x), from_none], self.secondary_emails)
        result["unconfirmed_emails"] = from_union([lambda x: from_list(
            lambda x: x, x), from_none], self.unconfirmed_emails)
        result["last_posted_at"] = self.last_posted_at.isoformat()
        result["last_seen_at"] = self.last_seen_at.isoformat()
        result["created_at"] = self.created_at.isoformat()
        result["ignored"] = from_bool(self.ignored)
        result["muted"] = from_bool(self.muted)
        result["can_ignore_user"] = from_bool(self.can_ignore_user)
        result["can_mute_user"] = from_bool(self.can_mute_user)
        result["can_send_private_messages"] = from_bool(
            self.can_send_private_messages)
        result["can_send_private_message_to_user"] = from_bool(
            self.can_send_private_message_to_user)
        result["trust_level"] = from_int(self.trust_level)
        result["moderator"] = from_bool(self.moderator)
        result["admin"] = from_bool(self.admin)
        result["title"] = from_str(self.title)
        result["badge_count"] = from_int(self.badge_count)
        result["custom_fields"] = to_class(CustomFields, self.custom_fields)
        result["time_read"] = from_int(self.time_read)
        result["recent_time_read"] = from_int(self.recent_time_read)
        result["primary_group_id"] = from_none(self.primary_group_id)
        result["primary_group_name"] = from_none(self.primary_group_name)
        result["flair_group_id"] = from_none(self.flair_group_id)
        result["flair_name"] = from_none(self.flair_name)
        result["flair_url"] = from_none(self.flair_url)
        result["flair_bg_color"] = from_none(self.flair_bg_color)
        result["flair_color"] = from_none(self.flair_color)
        result["featured_topic"] = from_none(self.featured_topic)
        result["timezone"] = from_str(self.timezone)
        result["pending_posts_count"] = from_int(self.pending_posts_count)
        result["can_edit"] = from_bool(self.can_edit)
        result["can_edit_username"] = from_bool(self.can_edit_username)
        result["can_edit_email"] = from_bool(self.can_edit_email)
        result["can_edit_name"] = from_bool(self.can_edit_name)
        result["uploaded_avatar_id"] = from_union(
            [from_int, from_none], self.uploaded_avatar_id)
        result["has_title_badges"] = from_union(
            [from_bool, from_none], self.has_title_badges)
        result["pending_count"] = from_int(self.pending_count)
        result["profile_view_count"] = from_int(self.profile_view_count)
        result["second_factor_enabled"] = from_union(
            [from_bool, from_none], self.second_factor_enabled)
        result["second_factor_backup_enabled"] = from_union(
            [from_bool, from_none], self.second_factor_backup_enabled)
        result["associated_accounts"] = from_list(
            AssociatedAccount.from_dict, self.associated_accounts)
        result["can_upload_profile_header"] = from_bool(
            self.can_upload_profile_header)
        result["can_upload_user_card_background"] = from_bool(
            self.can_upload_user_card_background)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["muted_category_ids"] = from_list(
            from_int, self.muted_category_ids)
        result["regular_category_ids"] = from_list(
            lambda x: x, self.regular_category_ids)
        result["watched_tags"] = from_list(lambda x: x, self.watched_tags)
        result["watching_first_post_tags"] = from_list(
            lambda x: x, self.watching_first_post_tags)
        result["tracked_tags"] = from_list(lambda x: x, self.tracked_tags)
        result["muted_tags"] = from_list(lambda x: x, self.muted_tags)
        result["tracked_category_ids"] = from_list(
            lambda x: x, self.tracked_category_ids)
        result["watched_category_ids"] = from_list(
            lambda x: x, self.watched_category_ids)
        result["watched_first_post_category_ids"] = from_list(
            from_int, self.watched_first_post_category_ids)
        result["system_avatar_upload_id"] = from_none(
            self.system_avatar_upload_id)
        result["system_avatar_template"] = from_union(
            [from_str, from_none], self.system_avatar_template)
        result["custom_avatar_upload_id"] = from_int(
            self.custom_avatar_upload_id)
        result["custom_avatar_template"] = from_str(
            self.custom_avatar_template)
        result["muted_usernames"] = from_list(
            lambda x: x, self.muted_usernames)
        result["ignored_usernames"] = from_list(
            lambda x: x, self.ignored_usernames)
        result["allowed_pm_usernames"] = from_list(
            lambda x: x, self.allowed_pm_usernames)
        result["mailing_list_posts_per_day"] = from_union(
            [from_int, from_none], self.mailing_list_posts_per_day)
        result["can_change_bio"] = from_union(
            [from_bool, from_none], self.can_change_bio)
        result["can_change_location"] = from_union(
            [from_bool, from_none], self.can_change_location)
        result["can_change_website"] = from_union(
            [from_bool, from_none], self.can_change_website)
        result["can_change_tracking_preferences"] = from_union(
            [from_bool, from_none], self.can_change_tracking_preferences)
        result["user_api_keys"] = from_list(
            lambda x: to_class(UserAPIKey, x), self.user_api_keys)
        result["user_auth_tokens"] = from_list(
            lambda x: to_class(UserAuthToken, x), self.user_auth_tokens)
        result["user_notification_schedule"] = from_union(
            [from_none, UserNotificationSchedule.from_dict], self.user_notification_schedule)
        result["use_logo_small_as_avatar"] = from_union(
            [from_bool, from_none], self.use_logo_small_as_avatar)
        result["sidebar_tags"] = from_list(
            lambda x: to_class(SidebarTag, x), self.sidebar_tags)
        result["sidebar_category_ids"] = from_list(
            from_int, self.sidebar_category_ids)
        result["display_sidebar_tags"] = from_union(
            [from_bool, from_none], self.display_sidebar_tags)
        result["cakedate"] = self.cakedate.isoformat()
        result["birthdate"] = from_none(self.birthdate)
        result["accepted_answers"] = from_int(self.accepted_answers)
        result["featured_user_badge_ids"] = from_list(
            from_int, self.featured_user_badge_ids)
        result["invited_by"] = from_none(self.invited_by)
        result["groups"] = from_list(lambda x: to_class(Group, x), self.groups)
        result["group_users"] = from_list(
            lambda x: to_class(GroupUser, x), self.group_users)
        result["user_option"] = from_union(
            [UserOption.from_dict, from_none], self.user_option)
        return result


def user_from_dict(s: Any) -> User:
    return User.from_dict(s)


def user_to_dict(x: User) -> Any:
    return to_class(User, x)


@dataclass
class UserInfo:
    user_badges: List[Any]
    user: User

    @staticmethod
    def from_dict(obj: Any) -> 'UserInfo':
        assert isinstance(obj, dict)
        user_badges = obj.get("user_badges")
        user = User.from_dict(obj.get("user"))
        return UserInfo(user_badges, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_badges"] = self.user_badges
        result["user"] = self.user.to_dict()
