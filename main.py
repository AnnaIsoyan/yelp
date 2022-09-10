from mymodules import save_document, extract_tar


extract_tar.extract_tar("tar_files/yelp_dataset.tar", 'json_files')

save_doc = save_document.SaveDocument('json_files', ['user', 'review', 'business'])
save_doc.save()
