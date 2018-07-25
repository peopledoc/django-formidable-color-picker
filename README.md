# Django Formidable Color Picker

**WARNING**: this module is not ready yet - it's targeting a future version of `django-formidable` ; you won't be able to use it right now.

This is a "Proof of Concept" external field for `django-formidable`. Regular / classic fields are all handled by the core `django-formidable` code, but there might be the need for a "business logic-related" field.

For the sake of the example, we've created a "color picker" abstract field here, that will be enable the following:

- [x] Forms can be created/updated with this `color_picker` type of field.
- [x] These fields would carry at least a `format` parameter (`rgb` or `hex`).
- [x] This `format` parameter will be checked when trying to save a form.
- [x] Serializing the form definition in JSON would also carry this field and its definition, so a "smart" front-end would be able to manipulate it in a "form builder" or a "form filler".
- [ ] When an end-user would submit a form using this form definition, the value selected by the user (the color) would have to be checked against a "form-data" validator, to make sure they have selected a correct color.

## Usage

* Install this module via `pip install -e ./` in your virtualenv
* Add `formidable_color_picker` to the ``INSTALLED_APPS``, preferrably right after `django-formidable`.
* Profit!

## License

Undefined yet. Anyway, you can't use me, you remember?
