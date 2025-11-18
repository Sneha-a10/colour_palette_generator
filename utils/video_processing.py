import cv2
import numpy as np


def get_representative_frames(video_path, max_frames=7, hist_threshold=0.35):
    """
    Intelligent frame selection:
    Selects frames where scene changes significantly using histogram difference.
    """

    cap = cv2.VideoCapture(video_path)
    frames = []
    prev_hist = None
    selected = 0

    while selected < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Compute histogram
        hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8],
                            [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        if prev_hist is None:
            frames.append(frame_rgb)
            prev_hist = hist
            selected += 1

        else:
            diff = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)

            # If scene changed meaningfully, pick this frame
            if diff > hist_threshold:
                frames.append(frame_rgb)
                prev_hist = hist
                selected += 1

    cap.release()
    return frames
