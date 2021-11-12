listPlots = """select owp.id, owp.catastral_id, owp.addres_name, owp.realtor_name, owt.name, ows.identification,
ows.name_owner, plo.name from public.owner_plost as owp
INNER JOIN owners as ows ON owp.owner_data = ows.id
INNER JOIN plost_type as plo ON owp.plost_type = plo.id
INNER JOIN owner_type as owt ON ows.type_owner = owt.id"""

listPlotById = """SELECT * FROM public.owner_plost WHERE id = {}"""

listPlotsType = """SELECT * FROM public.plost_type;"""
listAllOwners = """SELECT * FROM public.owners;"""

insertPlots = """INSERT INTO public.owner_plost(catastral_id, plost_type, addres_name, realtor_name, owner_data) VALUES ('{}', {}, '{}', '{}', {});"""
updatePlots = """UPDATE public.owner_plost
	SET catastral_id='{}', plost_type={}, addres_name='{}', realtor_name='{}', owner_data={} WHERE id = {};"""
deletePlots = "DELETE FROM public.owner_plost WHERE id = {};"
