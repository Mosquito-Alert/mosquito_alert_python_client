# PhotoPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**BoundingBox**](BoundingBox.md) |  | 
**insect_confidence** | **float** | Insect confidence | 
**predicted_class** | **str** |  | [optional] 
**threshold_deviation** | **float** |  | 
**scores** | [**PredictionScore**](PredictionScore.md) |  | 
**classifier_version** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from mosquito_alert_api.models.photo_prediction import PhotoPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoPrediction from a JSON string
photo_prediction_instance = PhotoPrediction.from_json(json)
# print the JSON string representation of the object
print(PhotoPrediction.to_json())

# convert the object into a dict
photo_prediction_dict = photo_prediction_instance.to_dict()
# create an instance of PhotoPrediction from a dict
photo_prediction_from_dict = PhotoPrediction.from_dict(photo_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

