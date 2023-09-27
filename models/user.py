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
