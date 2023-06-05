import pygame


def load_image(path: str) -> pygame.Surface:
    return pygame.transform.scale_by(pygame.image.load(path))


def load_images(path: str, rects: list[tuple[int, int, int, int]]) -> list[pygame.Surface]:
    return [pygame.transform.scale_by(surf) for surf in clips(pygame.image.load(path), rects)]


def clip(surf: pygame.Surface, rect: tuple[int, int, int, int]) -> pygame.Surface:
    handle_surf = surf.copy()
    clip_rect = pygame.Rect(*rect)
    handle_surf.set_clip(clip_rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def clips(surf: pygame.Surface, rects: list[tuple[int, int, int, int]]) -> list[pygame.Surface]:
    return [clip(surf, rect) for rect in rects]


def rotate(image, pos, originPos, angle):
    """
    :param image: 이미지
    :param pos: 위치
    :param originPos: 회전 위치
    :param angle: 각도
    :return : 회전된 이미지
    """

    # calculate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    return rotated_image, origin
