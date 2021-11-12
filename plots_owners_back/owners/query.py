listOwners = """SELECT own.id, identification, name_owner, ownty.name FROM public.owners as own
INNER JOIN public.owner_type as ownty ON own.type_owner = ownty.id"""
listOwnerType = """SELECT * FROM public.owner_type"""

listById = """SELECT * FROM public.owners WHERE identification = '{}'"""
getTypeOwner = """SELECT type_owner FROM public.owners WHERE id = {}"""
insertOwners = """INSERT INTO public.owners(type_owner, identification, name_owner)VALUES ({}, '{}', '{}');"""
updateOwners = """UPDATE public.owners SET type_owner={}, identification='{}', name_owner='{}' WHERE id = {};"""
deleteOwners = "DELETE FROM public.owners WHERE identification = '{}';"
