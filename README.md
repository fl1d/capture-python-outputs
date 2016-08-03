# capture-python-outputs

A simple Python module capturing text outputs printed in python console and saving them as a file.

## Example usage

### Capturing and saving all outputs.

   ```python
   import cptprint
   ```

   By default, all printed text outputs will be saved in a file named `output_date_time.log`. It won't affect the outputs in console.

### Capturing and saving specified outputs.

```python
import cptprint
cptprint.para(part_capture_flag=True)
# print something A
cptprint.begin()
# print something B
cptprint.stop()
# print something C
```

Only B parts outputs will be captured and saved.  
