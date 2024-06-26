import os
from typing import Union

from ..utils.responses import Responses
from ..schemas.data_validators import Validators
from ..libs.database import Session
from ..models.files import Files as FilesModel

class Delete:
	@staticmethod
	def delete(file: str) -> Union[Responses.json, Responses.error]:
		"""
		Deletes a specified file from the uploads directory if the file name is valid.

		Parameters:
		- file (str): The name of the file to be deleted.

		Returns:
		- A JSON response indicating the outcome of the delete operation. If the file name
			is deemed invalid by the Validators, it returns an error response. If the deletion
			is successful, it returns a success message.

		Note:
		- The file name is validated using Validators.file.basic to prevent directory traversal attacks.
		- The file to be deleted is assumed to have a '.txt' extension and to be located in the './uploads' directory.
		"""
		# Validate the file name to prevent directory traversal attacks
		if Validators.file.basic(file):
			# If the file name is invalid, return an error response
			return Responses.error(err=True, status=400, message="Nombre no valido")

		# Attempt to delete the file from the uploads directory
		with Session() as db:
			# Find the file record in the database
			query = db.query(FilesModel).filter(FilesModel.name == file + ".txt").first()
			if query:
				# Delete the found record
				db.delete(query)
				db.commit()
			else:
				# If the file does not exist in the database, return an error response
				return Responses.error(err=True, status=404, message="Archivo no encontrado")

		# Return a success response if the file has been deleted
		return Responses.json(status=200, data=None, message="Archivo eliminado con éxito")