from dataclasses import dataclass



@dataclass
class PostScheme:
    title: str | None = None
    author: str = "Without author"
    text: str | None = None
    
    
@dataclass
class PostResponseSchema:
    key: str | None = None


@dataclass
class ImageResponseSchema:
    path: str | None = None