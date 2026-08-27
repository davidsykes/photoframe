from viewer.src.status.viewer_options import ViewerOptions


class ViewerOptionsLoader:
    def load_viewer_options(self, options):
        opts = ViewerOptions()
        for option in options:
            if option == 'si':
                opts.show_image_names = True
        return opts