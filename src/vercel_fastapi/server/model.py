from pydantic import BaseModel


class NoteSchema(BaseModel):
    title: str | None
    content: str | None

    class Config:
        schema_extra = {
            "example": {
                "title": "LogRocket.",
                "content": "Logrocket is the most flexible publishing company "
                + "for technical authors. From editors to payment, the "
                + "process is too flexible and that's what makes it great.",
            }
        }
