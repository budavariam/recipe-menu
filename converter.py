import json

def json_to_latex(data):
    latex = []
    for day in data["days"]:
        latex.append(f"\\section{{{day['day']}}}")
        for meal in day["meals"]:
            latex.append("\\sordisz")
            latex.append(f"\\subsection{{{meal['type']}: {meal['name']}}}")
            latex.append("\\begin{itemize}")
            for ing in meal["ingredients"]:
                latex.append(f"    \\item {ing['amount']} {ing['item']}".strip())
            latex.append("\\end{itemize}")
            latex.append(f"\\textbf{{Kalória:}} {meal['calories']} kcal \\\\")
            latex.append(f"\\textbf{{Rost:}} {meal['fiber']} \\\\")
            latex.append(f"\\textbf{{Elkészítés:}} {meal['instructions']}\n")
        latex.append("\\newpage")
    
    latex.append("\\section{Hozzávalók összesítése}")
    latex.append("\\begin{multicols}{2}")
    for category, items in data["shopping_list"].items():
        latex.append(f"\\subsection{{{category}}}")
        latex.append("\\begin{itemize}")
        for item in items:
            latex.append(f"    \\item {item}")
        latex.append("\\end{itemize}\n")
    latex.append("\\end{multicols}")
    return "\n".join(latex)

if __name__ == "__main__":
    with open("menu.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    tex_code = json_to_latex(data)
    with open("menu.tex", "w", encoding="utf-8") as f:
        f.write(tex_code)
