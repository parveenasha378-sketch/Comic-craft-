from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models import ComicRequest
from app.gemini_client import generate_outline, generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

    @router.post("/generate")
    def generate_comic(
        request: Request,
            story_prompt: str = Form(...),
                character_name: str = Form(...),
                    setting: str = Form(...),
                        story_tone: str = Form(...),
                            art_style: str = Form(...)
                            ):
                                outline = generate_outline(story_prompt, character_name, setting, story_tone, art_style)
                                    story_panels = generate_story(outline, story_prompt)

                                        for panel in story_panels:
                                                img_path = generate_image(panel["image_prompt"])
                                                        panel["image_path"] = img_path

                                                            comic_layout = build_comic_layout(story_panels)
                                                                pdf_path = save_pdf(comic_layout, character_name)

                                                                    return templates.TemplateResponse("comic_preview.html", {
                                                                            "request": request,
                                                                                    "panels": comic_layout,
                                                                                            "pdf_path": pdf_path,
                                                                                                    "pdf_url": f"/{pdf_path}",
                                                                                                            "character": character_name
                                                                                                                })

                                                                                                                @router.post("/generate-comic/json")
                                                                                                                def generate_comic_json(data: ComicRequest):
                                                                                                                    outline = generate_outline(data.story_prompt, data.character_name, data.setting, data.story_tone, data.art_style)
                                                                                                                        story_panels = generate_story(outline, data.story_prompt)
                                                                                                                            for panel in story_panels:
                                                                                                                                    panel["image_path"] = generate_image(panel["image_prompt"])
                                                                                                                                        layout = build_comic_layout(story_panels)
                                                                                                                                            pdf_path = save_pdf(layout, data.character_name)
                                                                                                                                                return {"panels": layout, "pdf_url": f"/{pdf_path}", "pdf_path": pdf_path}

                                                                                                                                                @router.get("/export-success")
                                                                                                                                                def export_success(request: Request):
                                                                                                                                                    return templates.TemplateResponse("export_success.html", {"request": request})

                                                                                                                                                    @router.post("/test-image")
                                                                                                                                                    def test_image(prompt: str = Form(...)):
                                                                                                                                                        path = generate_image(prompt)
                                                                                                                                                            return {"url": f"/{path}", "path": path}