from fastapi import FastAPI, Query, Body, HTTPException

app = FastAPI(title="Mini Blog")

BLOG_POST = [
  {"id": 1, "title": "Hello from FastAPI", "content": "The first fast api post"},
  {"id": 2, "title": "Second Post FastAPI", "content": "The second fast api post 2"},
  {"id": 3, "title": "Django vs FastAPI", "content": "Fast api is faster because is called fast xd"},
]

@app.get("/")
def home():
  return {'message': 'Welcome to mini blog'}

@app.get("/posts")
def list_posts(query: str | None = Query(default = None, description = "Text for title search")):
  
  if query:
    # LIST COMPREHENSION
    results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
    
    # NAIVE APPROACH
    # results = []
    # for post in BLOG_POST:
    #   if query.lower() in post["title"].lower():
    #     results.append(post)
    
    return {"data": results, "query": query}
    
  return {"data": BLOG_POST}

@app.get("/posts/{post_id}")
def get_post(post_id: int, include_content: bool | None = Query(default = True, description = "Blog content toggler")):
  for post in BLOG_POST:
      if post["id"] == post_id:
        return { "data": post } if include_content == True else { "data": { "id": post["id"], "title": post["title"] } }
  return { "error": "Post not found" }


@app.post("/posts")
# Body's parenthesis content:
# when we use None it means that is going to be optional
# elipsis(...) mean that there is not content but is required
def create_post(post:dict = Body(...)):
  if "title" not in post or "content" not in post:
    return { "error": "Content and Title are required"}
  
  if not str(post['title']).strip():
    return {"error": "Title cannot be empty"}
  
  # id is iterable in terms of blog post length
  # not optimal for prod. obviously
  new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
  new_post = { "id": new_id, "title": post["title"], "content": post["content"] }
  
  BLOG_POST.append(new_post)
  return { "message": "Post created", "data": new_post}

@app.put("/posts/{post_id}")
def update_post(post_id: int, data: dict = Body(...)):
  for post in BLOG_POST:
    if post["id"] == post_id:
      if "title" in data: post["title"] = data["title"]
      if "content" in data: post["content"] = data["content"]
      return {"message": "Updated post", "data": post }
  
  
  raise HTTPException(status_code = 404, detail= "Post wasn't found.")


@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
  for index, post in enumerate(BLOG_POST):
    if post["id"] == post_id:
      BLOG_POST.pop(index)
      return
    
  raise HTTPException(status_code=404, detail="Post not found.")