"""Createcount Migration."""

from masoniteorm.migrations import Migration


class Createcount(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("createcounts") as table:
            table.increments("id")
            table.unsigned_integer("count")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("createcounts")
