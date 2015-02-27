from django.conf.urls import patterns, include, url

from django.conf import settings

from .feeds import (AwardsRecentFeed, AwardsByUserFeed, AwardsByBadgeFeed,
                    BadgesRecentFeed, BadgesByUserFeed)
from . import views


urlpatterns = patterns('badger.views',
    url(r'^$', 'badges_list', name='badger.badges_list'),
    url(r'^staff_tools$', 'staff_tools',
        name='badger.staff_tools'),
    url(r'^tag/(?P<tag_name>.+)/?$', 'badges_list',
        name='badger.badges_list'),
    url(r'^awards/?', 'awards_list',
        name='badger.awards_list'),
    url(r'^badge/(?P<slug>[^/]+)/awards/?$', 'awards_list',
        name='badger.awards_list_for_badge'),
    url(r'^badge/(?P<slug>[^/]+)/awards/(?P<id>\d+)\.json$', 'award_detail',
        kwargs=dict(format="json"),
        name='badger.award_detail_json'),
    url(r'^badge/(?P<slug>[^/]+)/awards/(?P<id>\d+)/?$', 'award_detail',
        name='badger.award_detail'),
    url(r'^badge/(?P<slug>[^/]+)/awards/(?P<id>\d+)/delete$', 'award_delete',
        name='badger.award_delete'),
    url(r'^badge/(?P<slug>[^/]+)/claims/(?P<claim_group>.+)\.pdf$', 'claims_list',
        kwargs=dict(format='pdf'),
        name='badger.claims_list_pdf'),
    url(r'^badge/(?P<slug>[^/]+)/claims/(?P<claim_group>[^/]+)/?$', 'claims_list',
        name='badger.claims_list'),
    url(r'^claim/(?P<claim_code>[^/]+)/?$', 'claim_deferred_award',
        name='badger.claim_deferred_award'),
    url(r'^claim/?$', 'claim_deferred_award',
        name='badger.claim_deferred_award_form'),
    url(r'^badge/(?P<slug>[^/]+)/award', 'award_badge',
        name='badger.award_badge'),
    url(r'^badge/(?P<slug>.+)\.json$', 'detail',
        kwargs=dict(format="json"),
        name='badger.detail_json'),
    url(r'^badge/(?P<slug>[^/]+)/?$', 'detail',
        name='badger.detail'),
    url(r'^users/(?P<username>[^/]+)/awards/?$', 'awards_by_user',
        name='badger.awards_by_user'),

    url(r'^create$', 'create',
        name='badger.create_badge'),
    url(r'^badge/(?P<slug>[^/]+)/nominate$', 'nominate_for',
        name='badger.nominate_for'),
    url(r'^badge/(?P<slug>[^/]+)/edit$', 'edit',
        name='badger.badge_edit'),
    url(r'^badge/(?P<slug>[^/]+)/delete$', 'delete',
        name='badger.badge_delete'),
    url(r'^badge/(?P<slug>[^/]+)/nominations/(?P<id>\d+)/?$', 'nomination_detail',
        name='badger.nomination_detail'),
    url(r'^users/(?P<username>[^/]+)/badges/?$', 'badges_by_user',
        name='badger.badges_by_user'),

    url(r'^feeds/(?P<format>[^/]+)/badges/?$', BadgesRecentFeed(),
        name="badger.feeds.badges_recent"),
    url(r'^feeds/(?P<format>[^/]+)/users/(?P<username>[^/]+)/badges/?$',
        BadgesByUserFeed(),
        name="badger.feeds.badges_by_user"),

    url(r'^feeds/(?P<format>[^/]+)/awards/?$',
        AwardsRecentFeed(), name="badger.feeds.awards_recent"),
    url(r'^feeds/(?P<format>[^/]+)/badge/(?P<slug>[^/]+)/awards/?$',
        AwardsByBadgeFeed(), name="badger.feeds.awards_by_badge"),
    url(r'^feeds/(?P<format>[^/]+)/users/(?P<username>[^/]+)/awards/?$',
        AwardsByUserFeed(), name="badger.feeds.awards_by_user"),
)