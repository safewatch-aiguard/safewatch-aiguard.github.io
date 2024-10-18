import os
import json

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def generate_video_data(root_dir='video'):
    video_data = []
    
    for category in os.listdir(root_dir):
        category_path = os.path.join(root_dir, category)
        if not os.path.isdir(category_path):
            continue
        
        if category == 'benign':
            for video_file in os.listdir(category_path):
                if video_file.endswith('.mp4'):
                    video_path = os.path.join(category_path, video_file)
                    txt_path = os.path.join(category_path, video_file.replace('.mp4', '.txt'))
                    
                    if os.path.exists(txt_path):
                        description, guardrail, explanation = read_text_file(txt_path)
                        video_data.append({
                            "category": category.capitalize(),
                            "videoPath": video_path.replace('\\', '/'),
                            "description": description,
                            "guardrail": guardrail,
                            "explanation": explanation
                        })
        else:
            for subcategory in os.listdir(category_path):
                subcategory_path = os.path.join(category_path, subcategory)
                if not os.path.isdir(subcategory_path):
                    continue
                
                for video_file in os.listdir(subcategory_path):
                    if video_file.endswith('.mp4'):
                        video_path = os.path.join(subcategory_path, video_file)
                        txt_path = os.path.join(subcategory_path, video_file.replace('.mp4', '.txt'))
                        
                        if os.path.exists(txt_path):
                            description, guardrail, explanation = read_text_file(txt_path)
                            video_data.append({
                                "category": category.capitalize(),
                                "subcategory": subcategory,
                                "videoPath": video_path.replace('\\', '/'),
                                "description": description,
                                "guardrail": guardrail,
                                "explanation": explanation
                            })
    
    return video_data

def save_json(data, filename='video_data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    video_data = generate_video_data()
    save_json(video_data)
    print(f"Generated video_data.json with {len(video_data)} entries.")