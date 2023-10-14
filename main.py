from fastapi import FastAPI

app = FastAPI(
    title='Noted API',
    description='This a simple note taking service',
    docs_url='/'
)


@app.get('/')
async def hello():
    return {'message': 'Hello World'}


@app.get('/notes')
async def get_all_notes():
    pass


@app.post('/notes')
async def create_note():
    pass


@app.get('/notes/{note_id}')
async def get_note_by_id(note_id):
    pass


@app.patch('/notes/{note_id}')
async def update_note(note_id):
    pass


@app.delete('/notes/{note_id}')
async def delete_note(note_id):
    pass
