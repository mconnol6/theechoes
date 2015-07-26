from django import template

register = template.Library()

#get value of field in a model
def getattribute(model, field):
	if (hasattr(model, field.name)):
		return getattr(model, field.name)
	else:
		return ''

register.filter('getattribute', getattribute)
