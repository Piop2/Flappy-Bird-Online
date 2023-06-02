import pygame


def load_image(path: str, scale: int = 1) -> pygame.Surface:
    return pygame.transform.scale_by(pygame.image.load(path), scale)


def load_images(path: str, rects: list[tuple[int, int, int, int]], scale: int = 1) -> list[pygame.Surface]:
    return [pygame.transform.scale_by(surf, scale) for surf in clips(pygame.image.load(path), rects)]


def clip(surf: pygame.Surface, rect: tuple[int, int, int, int]) -> pygame.Surface:
    handle_surf = surf.copy()
    clip_rect = pygame.Rect(*rect)
    handle_surf.set_clip(clip_rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def clips(surf: pygame.Surface, rects: list[tuple[int, int, int, int]]) -> list[pygame.Surface]:
    return [clip(surf, rect) for rect in rects]
