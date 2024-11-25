from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drones.models import Person
from drones import views


class PersonTests(APITestCase):
    def post_person(self, name, old):
        url = reverse("person-list")
        data = {"name": name,"old": old }
        response = self.client.post(url, data, format="json")
        return response

    # Testa o método POST
    def test_post_and_get_person(self):
        new_person_name = "Olavo"
        new_person_old = 20
        response = self.post_person(new_person_name,new_person_old)
        print("PK {0}".format(Person.objects.get().pk))
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Person.objects.count())
        self.assertEqual(new_person_name, Person.objects.get().name)
        self.assertEqual(new_person_old, Person.objects.get().old)
      
        
    #   # Testa o critério de unicidade de nome de uma categoria de drone
    # def test_post_existing_drone_category_name(self):
    #     new_drone_category_name = "Duplicated Copter"
    #     response1 = self.post_drone_category(new_drone_category_name)
    #     self.assertEqual(status.HTTP_201_CREATED, response1.status_code)
    #     response2 = self.post_drone_category(new_drone_category_name)
    #     print(response2)
    #     self.assertEqual(status.HTTP_400_BAD_REQUEST, response2.status_code)
           
    #  # Testa o retorno de coleção de categorias de drone
    # def test_get_drone_categories_collection(self):
    #     new_drone_category_name = "Super Copter"
    #     self.post_drone_category(new_drone_category_name)
    #     url = reverse("dronecategory-list")
    #     response = self.client.get(url, format="json")
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     # Verifica existência de um elemento na resposta
    #     self.assertEqual(1, response.data["count"])
    #     self.assertEqual(new_drone_category_name, response.data["results"][0]["name"])
     
    #    # Testa a possibilidade de update do campo nome
    # def test_update_drone_category(self):
    #     drone_category_name = "Category Initial Name"
    #     response = self.post_drone_category(drone_category_name)
    #     url = reverse("dronecategory-detail", args=[response.data["pk"]])
    #     updated_drone_category_name = "Updated Name"
    #     data = {"name": updated_drone_category_name}
    #     patch_response = self.client.patch(url, data, format="json")
    #     self.assertEqual(status.HTTP_200_OK, patch_response.status_code)
    #     self.assertEqual(updated_drone_category_name, patch_response.data["name"])
     
    #   # Testa o retorno de uma única categoria de drone pelo id
    # def test_get_drone_category(self):
    #     drone_category_name = "Easy to retrieve"
    #     response = self.post_drone_category(drone_category_name)
    #     url = reverse("dronecategory-detail", args=[response.data["pk"]])
    #     get_response = self.client.get(url, format="json")
    #     self.assertEqual(status.HTTP_200_OK, get_response.status_code)
    #     self.assertEqual(drone_category_name, get_response.data["name"])