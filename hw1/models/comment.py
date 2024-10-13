from datetime import datetime


class Comment:
    def __init__(self, author_id: int, text: str) -> None:
        self.author_id: int = author_id
        self.text: str = text
        self.create_data: datetime = datetime.now()
        self.update_data: datetime = self.create_data
        self.like_count: int = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1
        self.update_data = datetime.now()

    def dislike(self) -> None:
        self.like_count -= 1
        self.update_data = datetime.now()

    def __repr__(self) -> str:
        return (
            f"Comment(author_id = {self.author_id}, "
            f"text = '{self.text}', "
            f"create_data = {self.create_data}, "
            f"update_data = {self.update_data}, "
            f"like_count = {self.like_count})"
        )
