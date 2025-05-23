#!/usr/bin/python3

import numpy as np


def compute_normalized_patch_descriptors(
    image_bw: np.ndarray, X: np.ndarray, Y: np.ndarray, feature_width: int
) -> np.ndarray:
    """Create local features using normalized patches.

    Normalize image intensities in a local window centered at keypoint to a
    feature vector with unit norm. This local feature is simple to code and
    works OK.

    Choose the top-left option of the 4 possible choices for center of a square
    window.

    Args:
        image_bw: array of shape (M,N) representing grayscale image
        X: array of shape (K,) representing x-coordinate of keypoints
        Y: array of shape (K,) representing y-coordinate of keypoints
        feature_width: size of the square window

    Returns:
        fvs: array of shape (K,D) representing feature descriptors
    """

    ###########################################################################
    # TODO: YOUR CODE HERE                                                    #
    ###########################################################################
    fvs = np.zeros((len(X), feature_width * feature_width))

    # Compute the feature vector for each point
    for i, (x, y) in enumerate(zip(X, Y)):
        # Extract the patch around the point
        patch = image_bw[int(y - feature_width // 2+1):int(y + feature_width // 2+1), int(x - feature_width // 2+1):int(x + feature_width // 2+1)]
        
        # Check if the patch size is as expected
        if patch.shape != (feature_width, feature_width):
            continue  # Skip this point if patch size is not as expected

        # Normalize the patch and flatten it into a feature vector
        fv = patch.flatten()
        fv = fv / np.linalg.norm(fv)
        
        fvs[i, :] = fv
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return fvs
