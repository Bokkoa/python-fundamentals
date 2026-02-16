from fastapi import FastAPI, Query, Body, HTTPException
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, List, Union

app = FastAPI(title="Mini Blog")

BLOG_POST = [
  {"id": 1, "title": "Hello from FastAPI", "content": "The first fast api post"},
  {"id": 2, "title": "Second Post FastAPI", "content": "The second fast api post 2"},
  {"id": 3, "title": "Django vs FastAPI", "content": "Fast api is faster because is called fast xd"},
]

class Tag(BaseModel):
  name: str = Field(..., min_length=2, max_length=30, description="Tag name")
  
class Author(BaseModel):
  name: str
  email: EmailStr

class PostBase(BaseModel):
  title: str
  content: str
  tags: List[Tag] = Field(default_factory=list) # using [] directly could cause reference issues.
  author: Optional[Author] = None

class PostCreate(BaseModel):
  title: str = Field(
    ..., # this makes the field required
    min_length=3,
    max_length=100,
    description="Post title",
    examples=["Mi first FastAPI Post!"]
  ),
  content: Optional[str] = Field(
    default="Unavailable content",
    min_length=10,
    description="Post content",
    examples=["This is a valid post content because we have more than 10 chars"]
  )
  
  # tags: Optional[List[Tag]] = []
  tags: Optional[List[Tag]] = Field(default_factory=list) # using [] directly could cause reference issues.
  author: Optional[Author] = None
  
  @field_validator("title")
  @classmethod
  def not_allowed_title(cls, value: str) -> str:
    if "spam" in value.lower():
      raise ValueError("Title cannot contain spam as word")
    return value
      
class PostUpdate(BaseModel):
  title: Optional[str] = Field(None, min_length=3, max_length=100)
  # an optional field from request with None as default value
  content: Optional[str] = None

class PostPublic(PostBase):
  id: int

class PostSummary(BaseModel):
  id: int
  title: str

@app.get("/")
def home():
  return {'message': 'Welcome to mini blog'}

@app.get("/posts", response_model=List[PostPublic])
def list_posts(query: str | None = Query(default = None, description = "Text for title search")):
  
  if query:
    # LIST COMPREHENSION
    results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
    
    # NAIVE APPROACH
    # results = []
    # for post in BLOG_POST:
    #   if query.lower() in post["title"].lower():
    #     results.append(post)
    
    # Manual response structure
    # return {"data": results, "query": query}
    return results
    
  return BLOG_POST # {"data": BLOG_POST}
                              # evaluate whether is PostPublic or PostSummary (if contains model or not)
@app.get("/posts/{post_id}", response_model=Union[PostPublic, PostSummary], response_description="Post Found")
def get_post(post_id: int, include_content: bool | None = Query(default = True, description = "Blog content toggler")):
  for post in BLOG_POST:
      if post["id"] == post_id:
        if not include_content:
          return { "id": post["id"], "title": post["title"] }  
        return post
  return HTTPException(status_code=404, detail="Post wasn't found")



@app.post("/posts", response_model=PostPublic, response_description="Post created")
# Body's parenthesis content:
# when we use None it means that is going to be optional
# elipsis(...) mean that there is not content but is required
def create_post(post: PostCreate):
  
  # id is iterable in terms of blog post length
  # not optimal for prod. obviously
  new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
  new_post = {"id": new_id,
              "title": post.title, 
              "content": post.content, 
              "tags": [tag.model_dump() for tag in post.tags],
              "author": post.author.model_dump() if post.author else None 
              }
  
  BLOG_POST.append(new_post)
  return new_post

@app.put("/posts/{post_id}", response_model=PostPublic, 
         response_description="Updated Post",
         response_model_exclude_none=True)
def update_post(post_id: int, data: PostUpdate):
  for post in BLOG_POST:
    if post["id"] == post_id:
      payload = data.model_dump(exclude_unset=True) # casting to dict (omiting empty values)
      if "title" in payload: post["title"] = payload["title"]
      if "content" in payload: post["content"] = payload["content"]
      return post

  raise HTTPException(status_code = 404, detail= "Post wasn't found.")


@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
  for index, post in enumerate(BLOG_POST):
    if post["id"] == post_id:
      BLOG_POST.pop(index)
      return
    
  raise HTTPException(status_code=404, detail="Post not found.")