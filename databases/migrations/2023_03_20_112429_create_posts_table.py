"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration
from masoniteorm.scopes import SoftDeletesMixin


class CreatePostsTable(Migration,SoftDeletesMixin):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.string("title")
            table.string("slug").unique()
            table.string("description")
            table.unsigned_integer("author_id")
            table.foreign("author_id").references("id").on("users")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
