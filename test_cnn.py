import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


# Charger le modèle entraîné
model_path = r"C:\Users\abdea\AppData\Roaming\jupyter\runtime\cnn.h5"
model = load_model(model_path)

# Définir les données du nouvel étudiant
new_data_dict = {
    'C121': [8],
    'C132': [10],
    'I111': [11],
    'I132': [20],
    'I143': [9],
    'I144': [7],
    'L111': [11],
    'L122': [13],
    'L133': [14],
    'M111': [9],
    'M112': [10],
    'M123': [10],
    'M124': [12],
    'M135': [14],
    'M136': [9],
    'M147': [9],
    'M148': [19],
    'P111': [11],
    'P112': [12],
    'P123': [11],
    'P124': [10],
    'P135': [11],
    'P146': [12],
    'P147': [13],
}

# Créer un DataFrame à partir des nouvelles données
new_data = pd.DataFrame(new_data_dict)

# Normaliser les nouvelles données en utilisant le StandardScaler déjà ajusté aux données d'entraînement
standard_scaler = StandardScaler()
new_data_normalized = standard_scaler.fit_transform(new_data)

# Faire des prédictions avec le modèle
predictions = model.predict(np.expand_dims(new_data_normalized, axis=-1))

# Décoder les prédictions en spécialités
label_encoder = LabelEncoder()
predicted_specialties = label_encoder.inverse_transform(np.argmax(predictions, axis=1))

# Afficher la spécialité prédite pour l'étudiant
print("Spécialité prédite pour l'étudiant :", predicted_specialties[0])
