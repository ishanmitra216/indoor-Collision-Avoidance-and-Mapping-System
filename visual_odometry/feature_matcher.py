import cv2

class FeatureMatcher:

    def __init__(self):
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    def match(self, des1, des2):

        if des1 is None or des2 is None:
            return []

        matches = self.bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        return matches[:200]