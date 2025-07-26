from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO('yolov8x.pt') 

# Train the model
model.train(
    data='data/data.yaml',
    epochs=200,
    imgsz=640,
    batch=16,
    device='3',           
    workers=4,
    project='logs/',
    name='yolov8-extra-large-lr5e-4-epochs-200',
    lr0=0.0005,
    optimizer='AdamW',        
    cos_lr=True,            
    amp=True ,
    patience=10                
)


# Load a pretrained YOLOv8 model
model = YOLO('yolov8x.pt') 

# Train the model
model.train(
    data='data/data.yaml',
    epochs=200,
    imgsz=640,
    batch=16,
    device='3',           
    workers=4,
    project='logs/',
    name='yolov8-extra-large-lr-1e-3-epochs-200',
    lr0=0.001,
    optimizer='AdamW',        
    cos_lr=True,            
    amp=True ,
    patience=10 ,               
)

# Load a pretrained YOLOv8 model
model = YOLO('yolov8l.pt') 

# Train the model
model.train(
    data='data/data.yaml',
    epochs=200,
    imgsz=640,
    batch=16,
    device='3',           
    workers=4,
    project='logs/',
    name='yolov8-large-lr5e-4-epochs-200',
    lr0=0.0005,
    optimizer='AdamW',        
    cos_lr=True,            
    amp=True,
    patience=10                
)

# Load a pretrained YOLOv8 model
model = YOLO('yolov8l.pt') 

# Train the model
model.train(
    data='data/data.yaml',
    epochs=200,
    imgsz=640,
    batch=16,
    device='3',           
    workers=4,
    project='logs/',
    name='yolov8-large-lr-1e-3-epochs-200',
    lr0=0.001,
    optimizer='AdamW',        
    cos_lr=True,            
    amp=True,
    patience=10       
)