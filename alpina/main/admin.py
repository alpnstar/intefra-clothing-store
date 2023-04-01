from django.contrib import admin

from main.models import GreetingIndex, CategoryGreeting, CollectionIndex, NoveltyIndex, PopularIndex, DiscountIndex


class GreetingsIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo", "category")
    list_display_links = ("id", "title")
    search_fields = ("title", )


class CategoryGreetingAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class CollectionIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class NoveltyIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class PopularIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class DiscountIndexAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_photo", "discount_on_photo", "photo", "title", "description", "sizes", "old_price",
                    "new_price")
    list_display_links = ("id", "ad_photo", "title", "photo")
    search_fields = ("title",)


admin.site.register(GreetingIndex, GreetingsIndexAdmin)
admin.site.register(CategoryGreeting, CategoryGreetingAdmin)
admin.site.register(CollectionIndex, CollectionIndexAdmin)
admin.site.register(NoveltyIndex, NoveltyIndexAdmin)
admin.site.register(PopularIndex, PopularIndexAdmin)
admin.site.register(DiscountIndex, DiscountIndexAdmin)
