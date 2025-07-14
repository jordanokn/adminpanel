from litestar import Controller, delete, get, patch, post, put


class CheckListsController(Controller):

    path = "/checklists"

    @get()
    async def get_check_lists(self):
        pass

    @get()
    async def get_check_list(self):
        pass

    @post()
    async def create_check_list(self):
        pass

    @post()
    async def create_check_list_record(self):
        pass
