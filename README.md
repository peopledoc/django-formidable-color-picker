# Django Formidable Color Picker

**WARNING**: this module is not ready yet - it's targeting a future version of `django-formidable` ; you won't be able to use it right now.

This is a "Proof of Concept" external field for `django-formidable`. Regular / classic fields are all handled by the core `django-formidable` code, but there might be the need for a "business logic-related" field.

For the sake of the example, we've created a "color picker" abstract field here, that will be enable the following:

- [x] Forms can be created/updated with this `color_picker` type of field.
- [ ] These fields would carry at least a `format` parameter (`rgb` or `hex`).
- [ ] This `format` parameter will be checked when trying to save a form.
- [ ] Serializing the form definition in JSON would also carry this field and its definition, so a "smart" front-end would be able to manipulate it in a "form builder" or a "form filler".


## License

Undefined yet. Anyway, you can't use me, you remember?