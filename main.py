import moviepy.editor as mp

audio = mp.AudioFileClip("MONTAGEM CORAL x VOIS SUR TON CHEMIN x HE'S BACK  (SLOWED  REVERB) [BRAZILIAN PHONK].mp3")
video1 = mp.VideoFileClip("Jujutsu Kaisen (Season 2)「AMV」Gods「4K 60FPS」.mp4")
final = video1.set_audio(audio)

final.write_videofile("JJKMontagemCoral.mp4")