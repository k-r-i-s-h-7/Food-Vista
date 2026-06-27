As global health consciousness rises, the need for automated, precise, and culturally inclusive dietary monitoring systems has become paramount. While existing food recognition technologies have made significant strides, they often struggle with the visual complexity of multi-
ingredient dishes and frequently lack optimization for regional cuisines, specifically Indian di-
etary habits. This report presents “Food Vista: A Food Detection and Nutritional
Analysis Pipeline,” an end-to-end intelligent system designed to bridge the gap between
visual food recognition and actionable health insights.
The proposed system leverages state-of-the-art deep learning architectures to perform a
multi-stage analysis of food images. By employing YOLOv8 for real-time object detection
and semantic segmentation, the pipeline accurately identifies diverse food items and isolates
specific ingredients within a dish. To overcome the limitations of Western-centric models, the
system is fine-tuned on comprehensive datasets including IndianFoodNet and FoodSeg103,
ensuring robust performance across both global and Indian cuisines.
Beyond simple classification, Food Vista introduces a quantitative dimension to dietary
tracking. By utilizing reference-based portion estimation and mapping detected items to ver-
ified nutritional databases, the system calculates precise macronutrient breakdowns (calories,
proteins, fats, and carbohydrates). Furthermore, the pipeline integrates a health risk assess-
ment module that generates personalized exercise recommendations based on caloric intake.
Developed as a full-stack application compatible with web and mobile platforms, Food Vista
transforms a single photograph into a comprehensive nutritional report. Experimental results
demonstrate high accuracy in classification and segmentation, proving the system’s effectiveness
as a viable tool for everyday users and fitness enthusiasts seeking to maintain a balanced lifestyle
through automated, real-time dietary surveillance
