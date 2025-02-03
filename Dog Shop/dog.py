from flask import Blueprint, render_template

dog_bp = Blueprint('dogs', __name__,)

dogs = [
    {'id': 1, 'name': 'Labrador', 'price': 500,'description': 'Friendly and energetic' },
    {'id': 2, 'name': 'German Shepherd', 'price': 1000,'description': 'Friendly,energetic and aggressive' },
    {'id': 3, 'name': 'Bulldog', 'price': 1500,'description': 'Friendly, energetic and protective' },
    {'id': 4, 'name': 'Golden Retriever', 'price': 500,'description': 'Friendly and energetic' },
    {'id': 5, 'name': 'French Bulldog', 'price': 2000,'description': 'Friendly and energetic' },
    {'id': 6, 'name': 'Siberian Husky', 'price': 3500,'description': 'Friendly and energetic' },
    {'id': 7, 'name': 'Beagle', 'price': 500,'description': 'Friendly and energetic' },
    {'id': 8, 'name': 'Alaskan Malamute', 'price': 4500,'description': 'Friendly and energetic' },
    {'id': 9, 'name': 'Poodle', 'price': 7500,'description': 'Friendly and energetic' },
    {'id': 10, 'name': 'Chihuahua', 'price': 8000,'description': 'Friendly and energetic' },
    {'id': 11, 'name': 'Australian Castle Dog', 'price': 1500,'description': 'Friendly and energetic' },
    {'id': 12, 'name': 'Dachshund', 'price': 6500,'description': 'Friendly and energetic' },
    {'id': 13, 'name': 'Rottweiler', 'price': 2500,'description': 'Friendly and energetic' },
    {'id': 14, 'name': 'Airedale Terrier', 'price': 5500,'description': 'Friendly and energetic' },
    {'id': 15, 'name': 'Border Collie', 'price': 7500,'description': 'Friendly and energetic' },
    {'id': 16, 'name': 'Australian Shepherd', 'price': 8500,'description': 'Friendly and energetic' },
    {'id': 17, 'name': 'Affenpinscher', 'price': 6500,'description': 'Friendly and energetic' },
    {'id': 18, 'name': 'American Staffordshire', 'price': 9500,'description': 'Friendly and energetic' },
    {'id': 19, 'name': 'Bichon Frise', 'price': 9500,'description': 'Friendly and energetic' },
    {'id': 20, 'name': 'Maltese dog', 'price': 5500,'description': 'Friendly and energetic' },
    {'id': 21, 'name': 'English Cocker spaniel', 'price': 7500,'description': 'Friendly and energetic' },
    {'id': 22, 'name': 'Anatolian Shepherd', 'price': 4500,'description': 'Friendly and energetic' },
    {'id': 23, 'name': 'Yorkshire Terrier', 'price': 8500,'description': 'Friendly and energetic' },
    {'id': 24, 'name': 'Afghan Hound', 'price': 8500,'description': 'Friendly and energetic' },
    {'id': 25, 'name': 'American Eskimo', 'price': 9500,'description': 'Friendly and energetic' },
    {'id': 26, 'name': 'Chow Chow', 'price': 11500,'description': 'Friendly and energetic' },
    {'id': 27, 'name': 'Pomeranian', 'price': 4500,'description': 'Friendly and energetic' },
    {'id': 28, 'name': 'Basset Hound', 'price': 9500,'description': 'Friendly and energetic' },
    {'id': 29, 'name': 'Newfoundland', 'price': 8500,'description': 'Friendly and energetic' },
    {'id': 30, 'name': 'Boston terrier', 'price': 4500,'description': 'Friendly and energetic' },
    {'id': 31, 'name': 'Bullmastiff', 'price': 5500,'description': 'Friendly and energetic' },
    {'id': 32, 'name': 'Cane Corso', 'price': 7500,'description': 'Friendly and energetic' },
    {'id': 33, 'name': 'Doberman', 'price': 8500,'description': 'Friendly and energetic' },
    {'id': 34, 'name': 'American Bully', 'price': 4500,'description': 'Friendly and energetic' },
    {'id': 35, 'name': 'Sarabi Dog', 'price': 7500,'description': 'Friendly and energetic' }
]

@dog_bp.route('/')
def home():
    return render_template('index.html')

@dog_bp.route('/list')
def dog_list():
    return render_template('dog_list.html', dogs = dogs)

@dog_bp.route('/<int:dog_id>')
def dog_details(dog_id):
    dog = next((dog for dog in dogs if dog['id'] ==dog_id),None)
    if dog:
        return render_template('dog_detail.html', dog = dog)
    return "Dog not found", 404