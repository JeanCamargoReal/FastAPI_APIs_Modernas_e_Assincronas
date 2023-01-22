from fastapi import FastAPI, HTTPException, Response, status, Path
from models import Curso

app = FastAPI()

cursos = {
    1: {"titulo": "Programação para leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmois e lógica de programação", "aulas": 87, "horas": 67},
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None,
                                         title="ID do curso",
                                         description='Deve ser entre 1 e 2',
                                         # gt = greater then
                                         gt=0,
                                         # lt = lower then
                                         lt=3)):
    try:
        curso = cursos[curso_id]

        return curso

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = dict(curso)
    cursos[next_id]["id"] = next_id

    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = dict(curso)
        curso.id = curso_id
        cursos[curso_id]["id"] = int(curso_id)

        return curso

    else:
        raise HTTPException(
            status_code=status.HTTP_404,
            detail=f"Não existe um curso com o id {curso_id}",
        )


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404,
            detail=f"Não existe um curso com o id {curso_id}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
